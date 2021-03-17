from django.db import models

# Create your models here.


class Clerk(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username + " " + self.password
