#/general
from django.http.response import JsonResponse
from apps.api.serializers import *
from django.db.models import Q
from datetime import date, timedelta
from django.http import HttpResponse
import random
#drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


#models
from apps.users.models import *
from apps.directory.models import *







#####################################
##  VIEWS MODULE USERS            ## 
#####################################

class CurrentUserView(APIView):
	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data)

class UserCreate(generics.CreateAPIView):
	permission_classes = (AllowAny,)
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


#

class PropertyList(generics.ListCreateAPIView):
	queryset = Property.objects.all()
	serializer_class = PropertySerializer



class PropertyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Property.objects.all()
	serializer_class = PropertySerializer

class ServiceList(generics.ListCreateAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

class ServicePropertyReadList(generics.ListCreateAPIView):
	queryset = ServiceProperty.objects.all()
	serializer_class = ServicePropertyReadSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['property']


class ServicePropertyPostList(generics.ListCreateAPIView):
	queryset = ServiceProperty.objects.all()
	serializer_class = ServicePropertyPostSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['property']


class ServicePropertyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceProperty.objects.all()
	serializer_class = ServicePropertyPostSerializer

class ReservationList(generics.ListCreateAPIView):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['code','property','user']

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer

class TransactionList(generics.ListCreateAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

class ServicePropertyCheckInternalList(generics.ListCreateAPIView):
	queryset = ServicePropertyCheckInternal.objects.all()
	serializer_class = ServicePropertyCheckInternalSerializer

class ServicePropertyCheckInternalDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServicePropertyCheckInternal.objects.all()
	serializer_class = ServicePropertyCheckInternalSerializer

class ServicePropertyCheckINList(generics.ListCreateAPIView):
	queryset = ServicePropertyCheckIN.objects.all()
	serializer_class = ServicePropertyCheckINSerializer

class ServicePropertyCheckINDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServicePropertyCheckIN.objects.all()
	serializer_class = ServicePropertyCheckINSerializer

class ServicePropertyCheckOUTList(generics.ListCreateAPIView):
	queryset = ServicePropertyCheckOUT.objects.all()
	serializer_class = ServicePropertyCheckOUTSerializer

class ServicePropertyCheckOUTDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServicePropertyCheckOUT.objects.all()
	serializer_class = ServicePropertyCheckOUTSerializer

class ServiceTransferList(generics.ListCreateAPIView):
	queryset = ServiceTransfer.objects.all()
	serializer_class = ServiceTransferSerializer

class ServiceTransferDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceTransfer.objects.all()
	serializer_class = ServiceTransferSerializer

class ServiceTourList(generics.ListCreateAPIView):
	queryset = ServiceTour.objects.all()
	serializer_class = ServiceTourSerializer

class ServiceTourDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceTour.objects.all()
	serializer_class = ServiceTourSerializer

class ServiceExtraListList(generics.ListCreateAPIView):
	queryset = ServiceExtraList.objects.all()
	serializer_class = ServiceExtraListSerializer

class ServiceExtraListDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceExtraList.objects.all()
	serializer_class = ServiceExtraListSerializer

class ServiceExtraList(generics.ListCreateAPIView):
	queryset = ServiceExtra.objects.all()
	serializer_class = ServiceExtraSerializer

class ServiceExtraDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ServiceExtra.objects.all()
	serializer_class = ServiceExtraSerializer