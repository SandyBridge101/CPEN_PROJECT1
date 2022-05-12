from django.urls import path
from . import views

urlpatterns=[
    path('dashboard/',views.dashboard,name="dash-page"),
    path("logout", views.logout_request, name= "logout"),
    path(" ", views.home, name= "home"),
    path('openfile/',views.file_open,name="open-file")
]
