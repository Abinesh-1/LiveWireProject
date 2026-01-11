# livewire-project/courses/urls.py
from django.urls import path
from . import views

app_name = "livewire"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="aboutus"),
    path("oldurl/", views.oldurl, name="oldurl"),
    path("newurl/", views.newurl, name="newurl"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("enroll/", views.enroll, name="enroll"),
    path("api/users/", views.api_users, name="api_users"),
]
