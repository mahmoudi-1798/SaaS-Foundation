import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "my_page"
    my_context = {
        "page_title": my_title, 
        "queryset": queryset
    }

    html_template = "home.html"

    PageVisit.objects.create(path=request.path)

    return render(request, html_template, my_context)