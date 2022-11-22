from django.contrib import admin
from django.urls import path,include

from django.conf.urls import url


from rest_framework.authtoken.views import obtain_auth_token



from rest_framework import permissions
 

from . import views


 

urlpatterns = [
    #custom
    path('auth/', obtain_auth_token), #login
    path('register/', views.UserCreate.as_view()),
    path('profile/', views.CurrentUserView.as_view()),

    #models users
    path('users/', views.UserList.as_view()),  
    path('users/<pk>', views.UserDetail.as_view()),

    path('property/', views.PropertyList.as_view()),  
    path('property/<pk>', views.PropertyDetail.as_view()),

    path('service/', views.ServiceList.as_view()),  
    path('service/<pk>', views.ServiceDetail.as_view()),

    path('property/service/', views.ServicePropertyList.as_view()),  
    path('property/service/<pk>', views.ServicePropertyDetail.as_view()),

    path('property/reservation/', views.ReservationList.as_view()),  
    path('property/reservation/<pk>', views.ReservationDetail.as_view()),

    path('property/reservation/transaction', views.TransactionList.as_view()),  
    path('property/reservation/transaction/<pk>', views.TransactionDetail.as_view()),

    path('property/check/', views.ServicePropertyCheckInternalList.as_view()),  
    path('property/check/<pk>', views.ServicePropertyCheckInternalDetail.as_view()),


    path('property/reservation/check/checkin', views.ServicePropertyCheckINList.as_view()),  
    path('property/reservation/check/checkin/<pk>', views.ServicePropertyCheckINDetail.as_view()),

    path('property/reservation/check/checkout', views.ServicePropertyCheckOUTList.as_view()),  
    path('property/reservation/check/checkout/<pk>', views.ServicePropertyCheckOUTDetail.as_view()),


    path('property/reservation/service/transfer', views.ServiceTransferList.as_view()),  
    path('property/reservation/service/transfer/<pk>', views.ServiceTransferDetail.as_view()),

    
    path('property/reservation/service/tour', views.ServiceTourList.as_view()),  
    path('property/reservation/service/tour/<pk>', views.ServiceTourList.as_view()),


    path('property/reservation/service/extra_list', views.ServiceExtraListList.as_view()),  
    path('property/reservation/service/extra_list/<pk>', views.ServiceExtraListDetail.as_view()),


    path('property/reservation/service/extra', views.ServiceExtraList.as_view()),  
    path('property/reservation/service/extra/<pk>', views.ServiceExtraDetail.as_view()),
 
 
]

