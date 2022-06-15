# Mapping urls

# include() function - Look for a match with regular expressions link back to our app's own urls.py file
#Manually adding it to urls.py file required


#Create another urls.py inside Django app folder ( first_app )
from django.conf.urls import url
from first_app import views

urlpatterns = [
    url("", views.index, name="index"),
] # in the new urls

# In the project files - urls.py insert
from django.conf.urls import include
urlpatterns = [
    path("", views.index, name="index"),
    path("first_app/", include("first_app.urls")),
    path('admin/', admin.site.urls),
]
#runserver - after the local server address add /name declared in path - /("first_app/") in the text above

# The applications can have their own urls.py file which we call in the PROJECT urls.py
