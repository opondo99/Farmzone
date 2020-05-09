from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from backend.common.models import AbstractBase


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

TITLE = (
    ('Miss', 'Miss'),
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
)


class FarmzoneUserManager(BaseUserManager):

    """A manager class for the FarmzoneUser class."""

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        extra_fields.setdefault('is_superuser', False)
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class FarmzoneUser(AbstractBase, AbstractBaseUser):

    """A class to hold FarmzoneUser record."""

    title = models.CharField(
        max_length=256, choices=TITLE, null=True, blank=True)
    first_name = models.CharField(max_length=256, null=True, blank=True)
    middle_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(
        max_length=256, unique=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(
        max_length=24, choices=GENDER, null=True, blank=True)

    objects = FarmzoneUserManager()

    USERNAME_FIELD = 'email'

    @property
    def user_names(self):
        """Compute the member name."""
        return '{} {} {} {}'.format(
            self.title or 'Mr',
            self.first_name or '',
            self.middle_name or '',
            self.last_name or '')

    def __str__(self):
        return "FarmzoneUser: {}".format(self.user_names)
