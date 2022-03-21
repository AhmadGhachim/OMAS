from pyexpat.errors import messages
import shutil
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import os
import random
import pathlib

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .DataProcessor import DataProcessor
from .WorkbookInitializer import workbook_initializer
# Create your views here.


@api_view(['GET'])
def testReceive(request):
      return Response("Baby Boyyyy")

@api_view(['POST'])
def testLogic(request):
      if "Excel files" not in os.listdir():
            os.mkdir("Excel files")
      if "Attendance files" not in os.listdir():
            os.mkdir("Attendance files")
      if "Class list" not in os.listdir():
            os.mkdir("Class list")

      if (len(os.listdir("Excel files")) != 0):
            os.remove("Excel files/" + os.listdir("Excel files")[0])
      if (len(os.listdir("Attendance files")) != 0):
            os.remove("Attendance files/" + os.listdir("Attendance files")[0])
      if (len(os.listdir("Class list")) != 0):
            os.remove("Class list/" + os.listdir("Class list")[0])

      meeting_file = request.FILES['serviceFile']
      meeting_file_path = default_storage.save("Attendance files/" + meeting_file.name , ContentFile(meeting_file.read()))

      class_list = request.FILES['databaseFile']
      class_list_path = default_storage.save("Class list/" + class_list.name , ContentFile(class_list.read()))


      new_class_list_name = class_list.name.split(".")[0]
      workbook_initializer(new_class_list_name, ("January", "October"), class_list_path)

      
      workbook_path = "Excel files/" + new_class_list_name + ".xlsx"
      dp = DataProcessor(workbook_path, meeting_file_path, request.data["meetingType"], 50, int(request.data["cutOffNum"]))
      dp.output_to_workbook()
      dp.output_to_text_file()
      dp.output_to_console()

      return HttpResponse(dp)

@api_view(['GET'])
def download(request):
      workbook_path = "Excel files/" + os.listdir("Excel files")[0]
      file_name = os.listdir("Excel files")[0]
      # file_name = os.listdir("Excel files")[0].split(".")[0] + ".xlsx"

      file_server = pathlib.Path(workbook_path)
      if not file_server.exists():
        messages.error(request, 'file not found.')
      else:
        file_to_download = open(str(file_server), 'rb')
        response = FileResponse(file_to_download, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename='+ file_name
        return response
      return redirect('')
