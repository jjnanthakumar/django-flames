# flames-game-site-using-Django
BASIC DJANGO SERVER COMMANDS:
-> django-admin startproject 'proj-name' (create new project directory)
-> python manage.py startapp 'app-name' (create new app) #make sure that app is connected with the respective project check urls.py file in both app as well as project
-> py manage.py makemigrations 'app-name' (this command is to migrate your models)
-> py manage.py migrate (this command is to create table)
-> py manage.py createsuperuser (it will create super admin user with respective username and password)
-> py manage.py collectstatic (to collect all static files to respective root folder)

*********************download this project only if you guyz know some basics of Django otherwise dont download it**********************
-->Before running this project in your machine see the requirements file, all pip packages must be installed in your respective virtual environment.
-->please ignore gitignore file which will be usefull only in production.
-->Before running this " py manage.py runserver " make sure in settings.py file DEBUG is set to True.(it will shows some errors in localmachine instead of 404 Error)
-->Here no need of database You just ignore it because its a simple site so database is not needed.
-->'fla' directory is main app where you can find respective codings.
-->please be aware of static files in settings.py if STATIC_ROOT is not properly configured then it will result in an error
***************************************************************************************************************************************

more info needed... refer here - https://docs.djangoproject.com/en/3.1/intro/tutorial01/
