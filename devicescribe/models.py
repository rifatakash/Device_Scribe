from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField()
    condition = models.CharField(max_length=100)
