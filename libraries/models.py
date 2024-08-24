from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=100)
    auther=models.CharField(max_length=100)
    active=models.BooleanField(default=True)


def __srt__(self):
    return self.name
