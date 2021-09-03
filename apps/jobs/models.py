from django.db import models

#import another models
from apps.directory.models import Company
from djrichtextfield.models import RichTextField

from apps.users.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class KeyResponsibility(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class SkillJobs(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Benefit(models.Model):
    img = models.ImageField(upload_to='benefits/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    tags = models.CharField(max_length=200)
    
    description = RichTextField()
    location = models.CharField(max_length=200,blank=True)
    salary = models.CharField(max_length=200,blank=True)
    type_contract = models.CharField(max_length=200,blank=True)
    schedule = models.CharField(max_length=200,blank=True)
    remote = models.BooleanField(default=False)

    keys = models.ManyToManyField(KeyResponsibility)
    skills = models.ManyToManyField(SkillJobs)
    benefit = models.ManyToManyField(Benefit)
    

    def __str__(self):
        return self.title


        




class JobApply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_apply = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)


class QuestionApply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    is_req = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class AnswerApply(models.Model):
    question = models.ForeignKey(QuestionApply, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.TextField()
    date_answer = models.DateTimeField(auto_now_add=True)