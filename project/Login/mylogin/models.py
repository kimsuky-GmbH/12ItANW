from django.db import models
from datetime import date

from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=200)
    password_hash = models.CharField(max_length=200)
    created_at = models.DateField(default=date.today)
    isVerified = models.BooleanField(default=False)

    def password_hasher(string):
        hashed_pw = make_password(string)
        return hashed_pw

    def password_checker(string, password_hash):
        return check_password(string, password_hash)
