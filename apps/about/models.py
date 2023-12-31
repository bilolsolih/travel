from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from solo.models import SingletonModel


class PhoneNumber(models.Model):
    phone_number = PhoneNumberField(_('Phone number'), unique=True)
    is_active = models.BooleanField(_('Active status'))

    class Meta:
        verbose_name = _('Phone number')
        verbose_name_plural = _('Phone numbers')

    def save(self, *args, **kwargs):
        if self.is_active and PhoneNumber.objects.exclude(pk=self.pk).filter(is_active=True).exists():
            PhoneNumber.objects.exclude(pk=self.pk).filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.phone_number)


class SocialMedia(models.Model):
    title = models.CharField(_('Title'), max_length=128, blank=True, null=True)
    icon = models.FileField(_('Icon'), upload_to='images/about/icons/')
    link = models.URLField(_('Link or username'))

    class Meta:
        verbose_name = _('Social media account')
        verbose_name_plural = _('Social media accounts')

    def __str__(self):
        return self.title if self.title else self.link


class Location(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    region = models.ForeignKey('base.Region', related_name='offices', on_delete=models.PROTECT, verbose_name=_('Region'))
    city = models.CharField(_('City'), max_length=128)

    iframe = models.TextField(_('iFrame'), blank=True, null=True)
    latitude = models.CharField(_('Latitude'), max_length=64, blank=True, null=True)
    longitude = models.CharField(_('Longitude'), max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        return f'{self.title} in {self.region}'


class FrequentlyAskedQuestion(models.Model):
    question = models.TextField(_('Question'))
    answer = models.TextField(_('Answer'))

    class Meta:
        verbose_name = _('Frequently asked question')
        verbose_name_plural = _('Frequently asked questions')

    def __str__(self):
        return self.question


class TermsAndConditions(SingletonModel):
    terms = RichTextField(_('Terms and conditions'))

    class Meta:
        verbose_name = _('Terms and conditions')
        verbose_name_plural = _('Terms and conditions')

    def __str__(self):
        return 'Terms and Conditions'
