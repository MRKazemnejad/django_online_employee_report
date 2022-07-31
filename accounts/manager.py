from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):

    def create_user(self,email,full_name,phone_number,password=None):
        if not email:
            raise ValueError('ایمیل وارد شده معتبر نمی باشد')
        if not full_name:
            raise ValueError('نام وارد شده معتبر نمی باشد')
        if not phone_number:
            raise ValueError('شماره تلفن وارد شده معتبر نمی باشد')
        user=self.model(email=self.normalize_email(email),full_name=full_name,phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,full_name,phone_number,password=None):
        user=self.create_user(email,full_name,phone_number,password)
        user.is_admin=True
        user.save(using=self._db)
        return user

