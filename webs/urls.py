from django.urls import path
from .views import Show
urlpatterns=[
    path('',Show,name='home'),
]