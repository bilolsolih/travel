from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.managers import UserManager
from apps.base.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from . import choices


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    # AUTHENTICATION FIELDS #
    phone_number = PhoneNumberField(_('Phone number'), max_length=15, unique=True)
    email = models.EmailField(_('Email'), unique=True, blank=True, null=True)
    is_verified = models.BooleanField(_('Verified status'), default=False)
    is_active = models.BooleanField(_('Active status'), default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    # PERSONAL INFO #
    first_name = models.CharField(_('First name'), max_length=128)
    middle_name = models.CharField(_('Middle name'), max_length=128, blank=True, null=True)
    last_name = models.CharField(_('Last name'), max_length=128)
    gender = models.CharField(_('Gender'), choices=choices.GENDER, max_length=10)
    birthdate = models.DateField(_('Birthdate'), blank=True, null=True)

    # SENSITIVE INFO #
    passport_picture = models.ImageField(_('Passport picture'), upload_to='images/accounts/passports/%Y/%m/%d/', blank=True, null=True)
    individual_pin = models.CharField(_('Individual PIN number'), max_length=14, blank=True, null=True)
    serial_number = models.CharField(_('Passport serial number'), max_length=9, blank=True, null=True)

    # ADDRESS #
    region = models.CharField(_('Region/City'), max_length=128)
    district = models.CharField(_('District'), max_length=128)

    # ACTIVITIES #
    balance = models.IntegerField(_('Balance'), default=0)

    # DISTINCT FIELDS #
    is_staff = models.BooleanField(_('Staff status'), default=False)

    # OTHERS #
    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['last_name', 'first_name', 'middle_name'])
        ]

    def __str__(self):
        return str(self.phone_number)


class AdminUser(User):
    def save(self, *args, **kwargs):
        self.is_superuser = True
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = _('Admin User')
        verbose_name_plural = _('Admin Users')


class RelatedPerson(TimeStampedModel):
    # AUTHENTICATION FIELDS #
    phone_number = models.CharField(_('Phone number'), max_length=15)
    email = models.EmailField(_('Email'), unique=True, blank=True, null=True)

    # PERSONAL INFO #
    first_name = models.CharField(_('First name'), max_length=128)
    middle_name = models.CharField(_('Middle name'), max_length=128, blank=True, null=True)
    last_name = models.CharField(_('Last name'), max_length=128)
    gender = models.CharField(_('Gender'), choices=choices.GENDER, max_length=10)
    birthdate = models.DateField(_('Birthdate'), blank=True, null=True)

    # SENSITIVE INFO #
    passport_picture = models.ImageField(_('Passport picture'), upload_to='images/accounts/passports/%Y/%m/%d/', blank=True, null=True)
    individual_pin = models.CharField(_('Individual PIN number'), max_length=14, blank=True, null=True)
    serial_number = models.CharField(_('Passport serial number'), max_length=9, blank=True, null=True)

    # ADDRESS #
    region = models.CharField(_('Region/City'), max_length=128)
    district = models.CharField(_('District'), max_length=128)

    class Meta:
        verbose_name = _('Related person')
        verbose_name_plural = _('Related people')
        indexes = [
            models.Index(fields=['last_name', 'first_name', 'middle_name'])
        ]

    def __str__(self):
        return self.phone_number
