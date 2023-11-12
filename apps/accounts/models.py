from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.accounts.managers import UserManager
from apps.base.models import TimeStampedModel
from . import choices


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    # AUTHENTICATION FIELDS #
    phone_number = PhoneNumberField(_('Phone number'), max_length=15, unique=True)
    is_verified = models.BooleanField(_('Verified status'), default=False)
    is_active = models.BooleanField(_('Active status'), default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    # PERSONAL INFO #
    first_name = models.CharField(_('First name'), max_length=128)
    last_name = models.CharField(_('Last name'), max_length=128)
    profile_photo = models.ImageField(_('Profile photo'), upload_to='images/accounts/profile_photos/%Y/%m/', blank=True, null=True)
    gender = models.CharField(_('Gender'), choices=choices.GENDER, max_length=10, blank=True, null=True)
    birthdate = models.DateField(_('Birthdate'), blank=True, null=True)

    # SENSITIVE INFO #
    passport_picture = models.ImageField(_('Passport picture'), upload_to='images/accounts/passports/%Y/%m/%d/', blank=True, null=True)
    individual_pin = models.CharField(_('Individual PIN number'), max_length=14, blank=True, null=True)
    serial_number = models.CharField(_('Passport serial number'), max_length=9, blank=True, null=True)

    # ADDRESS #
    region = models.ForeignKey('base.Region', related_name='users', on_delete=models.PROTECT, blank=True, null=True, verbose_name=_('Region'))
    district = models.CharField(_('District'), max_length=128, blank=True, null=True)

    # ACTIVITIES #
    balance = models.IntegerField(_('Balance'), default=0)
    liked_packages = models.ManyToManyField('packages.Package', related_name='liked_users', blank=True, verbose_name=_('Liked packages'))

    # DISTINCT FIELDS #
    is_staff = models.BooleanField(_('Staff status'), default=False)

    # OTHERS #
    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['last_name', 'first_name'])
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
    responsible = models.ForeignKey('accounts.User', related_name='related_people', on_delete=models.CASCADE, verbose_name=_('Responsible person'))
    phone_number = models.CharField(_('Phone number'), max_length=15)
    is_phone_number_same = models.BooleanField(_('Is phone number the same?'))
    email = models.EmailField(_('Email'), unique=True, blank=True, null=True)

    # PERSONAL INFO #
    first_name = models.CharField(_('First name'), max_length=128)
    last_name = models.CharField(_('Last name'), max_length=128)
    gender = models.CharField(_('Gender'), choices=choices.GENDER, max_length=10)
    birthdate = models.DateField(_('Birthdate'), blank=True, null=True)

    # SENSITIVE INFO #
    passport_picture = models.ImageField(_('Passport picture'), upload_to='images/accounts/passports/%Y/%m/%d/', blank=True, null=True)
    individual_pin = models.CharField(_('Individual PIN number'), max_length=14, blank=True, null=True)
    serial_number = models.CharField(_('Passport serial number'), max_length=9, blank=True, null=True)

    # ADDRESS #
    region = models.ForeignKey('base.Region', related_name='related_users', on_delete=models.PROTECT, null=True, blank=True, verbose_name=_('Region/City'))
    district = models.CharField(_('District'), max_length=128)
    is_address_same = models.BooleanField(_('Is address the same?'))

    class Meta:
        verbose_name = _('Related person')
        verbose_name_plural = _('Related people')
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]

    def save(self, *args, **kwargs):
        if self.is_address_same:
            self.region = self.responsible.region
            self.district = self.responsible.district
        if self.is_phone_number_same:
            self.phone_number = self.responsible.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number


class VerifiedPhoneNumber(models.Model):
    phone_number = models.CharField(_('Phone number'), max_length=15, unique=True)

    class Meta:
        verbose_name = _('Verified phone number')
        verbose_name_plural = _('Verified phone numbers')
        indexes = [
            models.Index(fields=('phone_number',))
        ]

    def __str__(self):
        return self.phone_number


class OTPCode(TimeStampedModel):
    phone_number = models.CharField(_('Phone number'), max_length=15)
    code = models.CharField(_('Code'), max_length=4)
    is_expired = models.BooleanField(_('Expired status'), default=False)

    class Meta:
        verbose_name = _('OTP code')
        verbose_name_plural = _('OTP codes')
        unique_together = ['phone_number', 'code', 'is_expired']
        indexes = [
            models.Index(fields=('phone_number', 'code', 'is_expired'))
        ]

    def __str__(self):
        return f'{self.phone_number} - {self.code}'
