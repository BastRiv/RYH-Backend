from django.db import models

from apps.users.models import User

from datetime import datetime    


# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=70)
    status = models.IntegerField(default=0) # 0 - Disponible 1- No disponible 2- Reservado 3- Ocupado  4-Limpieza 5- Mantencion
    image_front_page = models.ImageField(upload_to="property_img", null=True, blank=True)
    image_1 = models.ImageField(upload_to="property_img",null=True,blank=True)
    image_2 = models.ImageField(upload_to="property_img",null=True,blank=True)
    image_3 = models.ImageField(upload_to="property_img",null=True,blank=True)
    image_4 = models.ImageField(upload_to="property_img",null=True,blank=True)
    image_5 = models.ImageField(upload_to="property_img",null=True,blank=True)
    image_6 = models.ImageField(upload_to="property_img",null=True,blank=True)
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    price= models.DecimalField(max_digits=10, decimal_places=0, default=0) 

    def __str__(self):
        return str(self.item) + ": $" + str(self.price)

    #other fields here

    def __str__(self):
        return self.name

class HistoryStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0) # 0 - Disponible 1- No disponible 2- Reservado 3- Ocupado actualmente 4-Limpieza 5- Mantencion
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Service(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class ServiceProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
        

class Reservation(models.Model):
    code = models.CharField(max_length=9)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now, blank=True)
    end_date = models.DateField(default=datetime.now, blank=True)

    #other fields here

    def __str__(self):
        return self.code

class Transaction(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    status = models.IntegerField(default=0)    
    type_transaction = models.IntegerField(default=0) # 0 - abono / 1 - checkin / 2 - checkout


class ServicePropertyCheckInternal(models.Model): #Mantenimiento
    service_property = models.ForeignKey(ServiceProperty, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class ServicePropertyCheckIN(models.Model): 
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    service_property = models.ForeignKey(ServiceProperty, on_delete=models.CASCADE)
    status = models.IntegerField(default=0) # 0 ok / 1 - con problemas / 2 - falla interna

class ServicePropertyCheckOUT(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    service_property = models.ForeignKey(ServiceProperty, on_delete=models.CASCADE)
    status = models.IntegerField(default=0) # 0 ok / 1 - con problemas / 2 - falla interna

class ServiceTransfer(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    type_transfer = models.IntegerField(default=0) # 1 ida / 2 vuelta / 3 full

class ServiceTour(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

class ServiceExtraList(models.Model):
    name = models.CharField(max_length=150)

class ServiceExtra(models.Model):
    service_extra = models.ForeignKey(ServiceExtraList, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)