from django.db import models
from django.contrib.auth.models import User
from enum import Enum

class PrivActions(Enum):
    Grant="Grant"
    Deny="Deny"

class UserActions(Enum):
    Add='Add'
    Remove='Remove'

class Privs(Enum):
    Read="Read"
    Modify="Modify"

class Product(models.Model):
    product=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.product

class Protocol(models.Model):
    protocol=models.CharField(max_length=100,unique=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

class CS096(models.Model):
    project=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    protocol=models.ForeignKey(Protocol,on_delete=models.SET_NULL,null=True)
    ecms_link=models.URLField(blank=True)
    request_date=models.DateTimeField(auto_now=True)
    requestor=models.CharField(max_length=100)
    approver=models.CharField(max_length=100)


class FileShare(models.Model):
    path = models.CharField(max_length=1000)
    group=models.CharField(max_length=100)
    action=models.CharField(max_length=10,
                            choices=[(i,i.value) for i in PrivActions ])
    priv=models.CharField(max_length=10,
                          choices=[(i,i.value) for i in Privs])
    cs096=models.ForeignKey(CS096,on_delete=models.CASCADE)


class UserAccess(models.Model):
    username=models.CharField(max_length=100)
    action=models.CharField(max_length=10,
                            choices=[(i,i.value) for i in UserActions ])
    group = models.CharField(max_length=100)
    cs096 = models.ForeignKey(CS096, on_delete=models.CASCADE)




