from django.urls import path
from .views import Show,Post_detail
urlpatterns=[
    path('',Show,name='home'),
    path('<int:pk>/',Post_detail.as_view(),name='detail'),
]