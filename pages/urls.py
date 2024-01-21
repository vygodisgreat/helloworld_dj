from django.urls import path
# import the path to power URLpattern
from .views import homePageView
# import all the views

urlpatterns = [
    path('', homePageView, name="home")
    # re, view and name?
]