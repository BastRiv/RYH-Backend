#general
from rest_framework.serializers import  *
from drf_extra_fields.fields import Base64ImageField
from rest_framework.validators import UniqueTogetherValidator
from datetime import date
from random import randint
from drf_extra_fields.fields import Base64ImageField

#models
from apps.users.models import *
from apps.directory.models import *
from apps.jobs.models import *

#
from django.core.mail import send_mail
from django.conf import settings




#########################################
##  SERIALIZERS MODULE USERS           ## 
#########################################

class UserSerializer(ModelSerializer):
	class Meta:		 
		model = User 
		fields = (
			'pk',
			'email',
			'first_name',
			'last_name',
			'join_date',
			'type_user',
			'is_active',
			'is_staff',
			'password',

		)

		validators = [
			UniqueTogetherValidator(
				queryset=User.objects.all(),
				fields=['email'],
				message="Usuario ya registrado",
			)
		]


	def create(self, validated_data):
		if User.objects.filter(email=validated_data['email']).count() != 0:
			pass
		else:
			user = User(
				email=validated_data['email'],
				username=validated_data['email'],
				first_name=validated_data['first_name'],
				last_name=validated_data['last_name'],
			)
			user.set_password(validated_data['password'])
			user.save()
			return user

	def update(self, instance, validated_data):
		instance.email = validated_data.get('email',instance.email)
		instance.username = validated_data.get('email',instance.username)
		instance.first_name = validated_data.get('first_name',instance.first_name)
		instance.last_name = validated_data.get('last_name',instance.last_name)
		instance.set_password(validated_data.get('password'))
		instance.save()
		return instance



#########################################
##  SERIALIZERS MODULE DIRECTORY       ## 
#########################################

class CompanySerializer(ModelSerializer):
	class Meta:		 
		model = Company 
		fields = (
			'pk',
			'name',
			'description',
		)

#########################################
##  SERIALIZERS MODULE JOBS       ## 
#########################################

class CategorySerializer(ModelSerializer):
	class Meta:		 
		model = Category 
		fields = (
			'pk',
			'name',
			'description',
		)

class KeyResponsibilitySerializer(ModelSerializer):
	class Meta:		 
		model = KeyResponsibility 
		fields = (
			'pk',
			'name',
			'description',
		)

class SkillJobsSerializer(ModelSerializer):
	class Meta:		 
		model = SkillJobs 
		fields = (
			'pk',
			'name',
			'description',
		)

class BenefitSerializer(ModelSerializer):
	class Meta:		 
		model = Benefit 
		fields = (
			'pk',
			'img',
			'name',
			'description',
		)

class JobSerializer(ModelSerializer):
	skills = SkillJobsSerializer(many=True)
	keys = KeyResponsibilitySerializer(many=True)
	benefit = BenefitSerializer(many=True)
	category = CategorySerializer(read_only=True)
	class Meta:		 
		model = Job 
		fields = (
			'pk',
			'title',
			'company',
			'category',
			'tags',

			'description',
			'location',
			'salary',
			'type_contract',
			'schedule',
			'remote',

			'keys',
			'skills',
			'benefit',


		)

class JobApplySerializer(ModelSerializer):
	class Meta:		 
		model = JobApply 
		fields = (
			'pk',
			'job',
			'user',
		)













