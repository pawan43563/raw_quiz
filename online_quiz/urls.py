from django.contrib import admin
from django.urls import path
from .views import *


app_name='online_quiz'

urlpatterns = [
    path('',Welcome,name='welcome'),
    path('rules',Rules,name='rules'),
    path('quiz',cache1,name='cache1'),
    path('cache3',cache3,name='cache3'),
]
