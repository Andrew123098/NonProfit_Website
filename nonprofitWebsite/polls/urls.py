from django.urls import path

from . import views

""" To call the view, we need to map it to a URL - and for this we need a URLconf.
To create a URLconf in the polls directory, create a file called urls.py. """

urlpatterns = [
    path('', views.index, name='index'),
]