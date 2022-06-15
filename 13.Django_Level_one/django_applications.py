# Django application performs a particular functionality
#for the entire web app. They can be plugged into other Django projects
#and are reusable

python manage.py startapp first_app(name)

#admin.py - Registering the models
#apps.py - Specific app configuration
#models.py - Data models and relationships between data
#test.py
#views.py - Functions for request and responses
#migrations folder - Database information relating to the models


#Return to settings.py and set the start of the app -> "INSTALLED_APPS", write in name of project folder
#Host a local server again to check if everything is working

# Host a view:
def index(request):
    return HttpResponse("Hello World!")
#Then connect to the urls.py
from first_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
]
