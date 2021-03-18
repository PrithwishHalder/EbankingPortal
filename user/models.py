from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    acc_no = models.CharField(max_length=200)
    balance = models.IntegerField()
    acc_type = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Transaction(models.Model):
    accountno = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    info = models.CharField(max_length=500)
    credit = models.IntegerField()
    debit = models.IntegerField()
    balance = models.IntegerField()

    def __str__(self):
        return self.accountno
