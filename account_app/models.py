from enum import nonmember
from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200, default='1234')
    email = models.EmailField(default='default@example.com')
    image = models.ImageField(upload_to='media/',blank=True,null=True)
    @classmethod
    def create_account(cls,id,name,email,password,image):
        accountobj = Account(
            id=id,
            name=name,
            email=email,
            password=password,
            image=image
        )
        accountobj.save()

        @classmethod
        def delete_account(cls, id):
            cls.objects.filter(pk=id).delete()

        def __str__(self):
            return self.name


