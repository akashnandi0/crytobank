from django.contrib.auth.models import User
from django.db import models


class Transferdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    account_number = models.CharField(max_length=100, default="SELF")
    amount = models.IntegerField()
    mpin = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mpin + self.account_number
