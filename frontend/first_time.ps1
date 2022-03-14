npm install
npm run build
cd ..
cd backend
python WorkbookInitializer.py workbook_initializer
Start-Process "http://127.0.0.1:8000/"
python manage.py runserver
