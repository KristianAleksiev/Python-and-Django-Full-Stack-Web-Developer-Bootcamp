conda create --name Virtual_environment django #- Create a new virtual environment
activate Virtual_environment  #- All installed versions will be available on it only
conda install django / pip install django
deactivate Virtual_environment

# Updating the packages

conda create --name Actual_name python=3.9

conda info --envs #- Listing all environmnets


django-admin startproject first_project

## Create a new folder - mkdir "name"

#After starting a project - With __init__.py the whole directory is treated as a package
#settings.py - Storing settings
#urls.py - Storing URL patterns - the different pages of the app -Regular expressions
#wsgi.py - Web server gateway interface
#manage.py -

python manage.py runserver # Hosting a local server
