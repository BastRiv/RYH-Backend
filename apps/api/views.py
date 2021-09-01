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






# TEST GENERATOR DATA

class GenerateView(APIView):
	def get(self,request):
		initial = 10
		limit = 10
		for x in range(initial,initial+limit):
			name_random = "Company "+str(x)
			description_random = "es una empresa de "+str(x)
			# Company.objects.create(name=name_random,description=description_random)
			random_title = "Backend Developer " + str(x)
			random_company = Company.objects.get(name=name_random)
			random_category = Category.objects.get(pk=random.randint(1,3))
			random_status = 0
			random_description = "description " + str(x)
			random_tags = "tags " + str(x)
			Job.objects.create(
				title = random_title,
				company = random_company,
				category = random_category,
				status = random_status,
				description = random_description,
				tags = random_tags,
			)
		return HttpResponse(status=200)

# 

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

 
#####################################
##  VIEWS MODULE DIRECTORY         ## 
#####################################

class CompanyList(generics.ListCreateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer

#####################################
##  VIEWS MODULE JOBS             ## 
#####################################

class CategoryList(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)	
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class JobList(generics.ListCreateAPIView):
	permission_classes = (AllowAny,)
	queryset = Job.objects.all()
	serializer_class = JobSerializer
	filter_backends = [DjangoFilterBackend,filters.SearchFilter]
	search_fields = ['title', 'description', 'tags']
	filter_fields = ['category']
	
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (AllowAny,)
	queryset = Job.objects.all()
	serializer_class = JobSerializer

class JobApplyList(generics.ListCreateAPIView):
	queryset = JobApply.objects.all()
	serializer_class = JobApplySerializer

class JobApplyDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = JobApply.objects.all()
	serializer_class = JobApplySerializer


