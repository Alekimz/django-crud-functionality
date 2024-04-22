from django.urls import path
from . import views

urlpatterns = [
    #path('registration/', views.registration, name='registration')
    path('login/', views.login, name='myloginpage'),
    path('register/', views.register, name='myregister'),
    path('courses/', views.courses, name='mycourses'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('', views.home, name='myhome'),
    path('addstudent1' , views.addstudent1, name='addingstudent'),



    path('addstudent1', views.addstudent1, name='addstudent1'),

    path('addstudent1', views.addstudent1, name='addstudent1'),
    path('editstudent1/<id>', views.editstudent1, name='editingtudent1'),
    path('updatestudent1/<id>', views.updatestudent1, name='updatingstudent1'),
    path('deletestudent1/<id>',views.deletestudent1)
]