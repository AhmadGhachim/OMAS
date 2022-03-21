from django.urls import include, path
from .views import download, testLogic, testReceive

urlpatterns = [
      path('hey', testReceive),
      path('processData', testLogic),
      path('download', download),
]