import datetime

from django.utils import timezone

from apps.discounts.models import Discount
from apps.packages.models import Package
from apps.base.models import Country

countries = [
    Country(title='Egypt'),
    Country(title='Pakistan'),
]

packages = [
    Package(title='Package 1', description='Description 1', country_id=1),
    Package(title='Package 2', description='Description 2', country_id=2)
]

date = timezone.now() + datetime.timedelta(days=5)

discounts = [
    Discount(title='Discount 1', description='Description 1', max_discount=25, expiry_date=date),
    Discount(title='Discount 2', description='Description 2', max_discount=15, expiry_date=date),
]


def create_discounts_and_packages():
    Country.objects.bulk_create(countries)
    Package.objects.bulk_create(packages)
    Discount.objects.bulk_create(discounts)
    for discount in Discount.objects.all():
        discount.packages.add(1, 2)


__all__ = ['create_discounts_and_packages']
