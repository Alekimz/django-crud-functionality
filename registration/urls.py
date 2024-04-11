from django.urls import path
from . import views

urlpatterns = [
    #path('registration/', views.registration, name='registration')
    path('login/', views.login, name='myloginpage'),
    path('register/', views.register, name='myregister'),
    path('courses/', views.courses, name='mycourses'),

    path('home/', views.home, name='myhome')

]
