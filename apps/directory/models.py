from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=70)

    #other fields here

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=70)

class ServiceProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Reservation(models.Model):
    code = models.CharField(max_length=9)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    #other fields here

    def __str__(self):
        return self.code

class Transaction(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    type_transaction = models.IntegerField(default=0) # 0 - abono / 1 - checkin / 2 - checkout


class ServicePropertyCheckInternal(models.Model):
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
    type_transfer = models.IntegerField(default=0) # 0 checkin / 1 checkout

class ServiceTour(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

class ServiceExtraList(models.Model):
    name = models.CharField(max_length=150)

class ServiceExtra(models.Model):
    service_extra = models.ForeignKey(ServiceExtraList, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)