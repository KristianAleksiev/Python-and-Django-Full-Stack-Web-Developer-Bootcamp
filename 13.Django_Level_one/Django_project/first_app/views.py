from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {"insert_me": "Hello, I am from views.py! with changed subfolder"}
    return render(request, "first_app/index.html", context=my_dict)
#Map this view to the urls.py file
