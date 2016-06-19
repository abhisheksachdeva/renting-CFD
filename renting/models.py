from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, address, city, first_name, last_name, contact_no, password):
        if not email:
            raise ValueError('Enter email')

        user = self.model(
            email=self.normalize_email(email=email),
            address=address,
            city=city,
            first_name=first_name,
            last_name=last_name,
            contact_no=contact_no

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, address, city, first_name, last_name, contact_no, password):
        user = self.create_user(email, address=address, city=city,
                                first_name=first_name, last_name=last_name,
                                contact_no=contact_no, password=password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, db_index=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    contact_no = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email

