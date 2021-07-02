from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_birthdays, name='list-birthdays'),
    path('new/', views.create_birthday, name='create-birthday'),
]