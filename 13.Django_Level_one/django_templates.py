# Django interacts with the website by templates - Static part of an HTML page

## Django template tags - Their syntax allows us to inject dynamic content that
## the Django App's views will produice, affecting the final HTML

#Need to create a templates directory and a subdirectory for each specific app's template
# IT GOES IN THE TOP LEVEL DIRECTORY (Django_project)

#Next step - Edit the DIR key inside the TEMPLATES dictionary in the settings.py file
#In order for it to be easily transferrable from one PC to another -> DIR path ->
#-> python os module -> DIR key inside the TEMPLATES dict.
# Then create html file called index.html inside of the templates/first_app directory
#Inside this html file inserting TEMPLATE TAGS (Secific syntax) -> Django Template Variable
#render() function


### Project folder -> settings.py -> BASE_DIR -> TEMPLATE_DIR = os.path.join(BASE_DIR, "templates") as a variable
### Pass in the TEMPLATE_DIR inside the settings.py TEMPLATES

# Inside the templates directory create index.html
#Django template tag -> {{{ insert_me }}} -> Editting views.py in the django app folder (first_app),
#edit the function - > New dictionary -> Key = variable in the Django template tag -> insert_me

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {"insert_me": "Hello, I am from views.py!"} # <===
    return render(request, "index.html", context=my_dict)

# Create a subfolder of templates called by the name of the django app
#Change the path in views.py in the app folder
