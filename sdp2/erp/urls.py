from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about),
    path('new_student/',views.new_student, name='newS'),
    path('view_student/',views.view_student, name='viewS'),
]
