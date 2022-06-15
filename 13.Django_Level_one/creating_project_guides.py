#Check django version - python -m django --version!!!


django-admin startproject Project_two
python manage.py startapp app_two
create a view

from django.http import HttpResponse
def index(request):
    return HttpResponse("text")


link with urls.py
from app_two import views
urlpatterns = [
    path("", views.index, name="index"),
]

change settings.py by adding django app name

Then run the server - python manage.py runserver
