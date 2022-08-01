from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):
    email=models.EmailField(unique=True)
    full_name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name','phone_number']

    def __str__(self):
        return f"{self.email}--{self.full_name}--{self.is_active}"

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class OtpCode(models.Model):
    code=models.IntegerField()
    phone_number=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code}--{self.phone_number}--{self.created}"