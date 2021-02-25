from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
SEX = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Transgender', 'Transgender')
]
ACCOUNT_TYPE = [
    ('Savings', 'Savings'),
    ('Current', 'Current'),
    ('NRI', 'NRI')
]
MARITAL_STATUS = [
    ('Married', 'Married'),
    ('Single', 'Single')
]
AGE_CHOICES = [tuple([x, x]) for x in range(1, 100)]


class createProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(choices=AGE_CHOICES, default="")
    sex = models.CharField(max_length=20, choices=SEX)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    alternate_phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.IntegerField()

    def __str__(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse('success', kwargs={'slug': self.slug})


class accountInfoModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100, unique=True)
    mpin = models.IntegerField(unique=True)
    balance = models.IntegerField(default=1000)
    acctype = models.CharField(max_length=20, choices=ACCOUNT_TYPE, default="Savings")

    def __str__(self):
        return self.account_number

    def get_absolute_url(self):
        return reverse('success', kwargs={'slug': self.slug})
