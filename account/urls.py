from django.urls import path
from . import views

urlpatterns = [
    #Post view
    path('login/', views.user_login, name= 'login'),
]