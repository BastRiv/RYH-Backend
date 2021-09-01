from django.contrib import admin
from django.urls import path,include

from django.conf.urls import url


from rest_framework.authtoken.views import obtain_auth_token



from rest_framework import permissions
 

from . import views


 

urlpatterns = [
    path('generate/', views.GenerateView.as_view()),
    #custom
    path('auth/', obtain_auth_token), #login
    path('register/', views.UserCreate.as_view()),
    path('profile/', views.CurrentUserView.as_view()),

    #models users
    path('users/', views.UserList.as_view()),  
    path('users/<pk>', views.UserDetail.as_view()),

    #models directory
    path('company/', views.CompanyList.as_view()),  
    path('company/<pk>', views.CompanyDetail.as_view()),
   
    #models Job
    path('company/', views.CompanyList.as_view()),  
    path('company/<pk>', views.CompanyDetail.as_view()),

    path('category/', views.CategoryList.as_view()),  
    path('category/<pk>', views.CategoryDetail.as_view()),

    path('job/', views.JobList.as_view()),  
    path('job/<pk>', views.JobDetail.as_view()),
    
    path('job/apply/', views.JobApplyList.as_view()),  
    path('job/apply/<pk>', views.JobApplyDetail.as_view()),
    
 
]

