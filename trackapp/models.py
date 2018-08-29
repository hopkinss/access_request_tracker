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
    product=models.ForeignKey(Product,related_name='protocols',   on_delete=models.CASCADE)

    def __str__(self):
        return self.protocol


class CS096(models.Model):
    project=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    protocol=models.ForeignKey(Protocol,on_delete=models.SET_NULL,null=True)
    request_date=models.DateTimeField(auto_now=True)
    requestor=models.CharField(max_length=100,null=True)
    approver=models.CharField(max_length=100,null=True)

    def get_date(self):
        return self.request_date.strftime("%d-%b-%Y")


class FileShare(models.Model):
    path = models.CharField(max_length=1000)
    group=models.CharField(max_length=100)
    action=models.CharField(max_length=10,
                            # choices=[(i,i.value) for i in PrivActions ]
                            choices=[("Grant",1)]
                            )
    priv=models.CharField(max_length=10,
                          choices=[("Modify",1)]
                          # choices=[(i,i.value) for i in Privs]
                          )
    cs096=models.ForeignKey(CS096,on_delete=models.CASCADE)


class UserAccess(models.Model):
    username=models.CharField(max_length=100)
    action=models.CharField(max_length=10,
                            choices=(("Add","Add"),("Remove","Remove")))
    group = models.CharField(max_length=100)
    cs096 = models.ForeignKey(CS096,related_name="useraccesses", on_delete=models.CASCADE)


