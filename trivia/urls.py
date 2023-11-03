from django.urls import path

from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", login_required(views.index), name="index"),
    path('create-username/', views.create_username, name='create_username'),
]
