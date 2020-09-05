# Preview
   If you want to see how projects looks like and like to have a preview of it than i have provided some Screenshots in the Screenshots Folder.


# 1.Installations
Clone repository


   git clone https://github.com/pawan43563/raw_quiz.git
   
   cd rawquiz
   
   
   pip install pipenv
   
   
   pipenv install django
   
   
   pipenv shell 
   
   
   pip install django-import-export
   
   
# 2.Migrations


  python manage.py makemigrations
  
  
  python manage.py migrate
  
# 3.Creating a SuperUser


   python manage.py createsuperuser
   
   
   After this command you will be asked to give your name and password which will be used for uploading questions answers in csv,pdf,etc format.

# 4.Running locally
   It will run on port 8000 by default.
   
   
   python manage.py runserver

# 5.Uploading Questions and Answers:
   http://127.0.0.1:8000/admin
   
   
   This Url will take you to the admin login panel and the username and password will the one which you provided during creating superuser in step 3.
   After logging in you will see online_quiz class in which there will be two models i.e. Questions and Answers Clicking on any one of them you will be redirected to that
   respective model and there will a option to import datasets and dataset is being provided in CSV folders.

# 6.Start the Quiz:
  http://127.0.0.1:8000
  
  
  This url will take you to the username page and you don't need to register just enter your name and start the quiz and your score along with your name will be displayed.
  
