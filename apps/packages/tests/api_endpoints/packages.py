from random import randint  # noqa

from django.utils import timezone

from apps.base.models import Country
from apps.packages.models import PackageFeature, PackagePicture, Destination, Trip, Package, Plan, PlanType
from apps.places.models import PopularPlace

countries = [
    Country(title='Egypt'),
    Country(title='Pakistan'),
    Country(title='United Arab Emirates'),
    Country(title='Saudi Arabia'),
]


popular_places = [
    PopularPlace(title='Popular place 1', picture='test_data/hotel.jpg', description='Description 1'),
    PopularPlace(title='Popular place 2', picture='test_data/motel.jpg', description='Description 2'),
    PopularPlace(title='Popular place 3', picture='test_data/villas.jpg', description='Description 3'),
    PopularPlace(title='Popular place 4', picture='test_data/accommodation_1.jpg', description='Description 4'),
    PopularPlace(title='Popular place 5', picture='test_data/accommodation_2.jpg', description='Description 5'),
    PopularPlace(title='Popular place 6', picture='test_data/accommodation_3.jpg', description='Description 6'),
]

package_features = [
    PackageFeature(title='Package Feature 1', description='Description 1', icon='test_data/icon.jpg'),
    PackageFeature(title='Package Feature 2', description='Description 2', icon='test_data/icon.jpg'),
    PackageFeature(title='Package Feature 3', description='Description 3', icon='test_data/icon.jpg'),
    PackageFeature(title='Package Feature 4', description='Description 4', icon='test_data/icon.jpg'),
    PackageFeature(title='Package Feature 5', description='Description 5', icon='test_data/icon.jpg'),
    PackageFeature(title='Package Feature 6', description='Description 6', icon='test_data/icon.jpg'),
    PackageFeature(title='Package Feature 7', description='Description 7', icon='test_data/icon.jpg'),
    PackageFeature(title='Package Feature 8', description='Description 8', icon='test_data/icon.jpg'),
    PackageFeature(title='Package Feature 9', description='Description 9', icon='test_data/icon.jpg'),
]
packages = [
    Package(title='Package 1', description='Description 1', country_id=1),
    Package(title='Package 2', description='Description 2', country_id=2),
    Package(title='Package 3', description='Description 3', country_id=3),
]

pictures = [
    PackagePicture(package_id=1, picture='test_data/package_1', is_main=True),
    PackagePicture(package_id=1, picture='test_data/package_2'),
    PackagePicture(package_id=2, picture='test_data/package_3', is_main=True),
    PackagePicture(package_id=2, picture='test_data/package_4'),
]

plan_types = [
    PlanType(title='Economy'),
    PlanType(title='Standard'),
    PlanType(title='Premium'),
]

plans = [
    Plan(package_id=1, type_id=1, price=1000, discount=0, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
    Plan(package_id=1, type_id=2, price=1000, discount=15, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
    Plan(package_id=1, type_id=3, price=1000, discount=20, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
    Plan(package_id=2, type_id=1, price=1000, discount=20, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
    Plan(package_id=2, type_id=2, price=1000, discount=15, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
    Plan(package_id=2, type_id=3, price=1000, discount=0, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
    Plan(package_id=3, type_id=1, price=1000, discount=10, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
    Plan(package_id=3, type_id=2, price=1000, discount=0, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
    Plan(package_id=3, type_id=3, price=1000, discount=15, discount_expiry_date='2024-12-30T12:00:00+05:00', description='Description'),
]

destinations = [
    Destination(package_id=1, city_id=1, duration=5),
    Destination(package_id=1, city_id=2, duration=5),
    Destination(package_id=2, city_id=3, duration=5),
    Destination(package_id=2, city_id=4, duration=5),
    Destination(package_id=3, city_id=1, duration=5),
    Destination(package_id=3, city_id=3, duration=5),
]

date = timezone.now().date()

trips = [
    Trip(package_id=1, start_date="2024-01-05", end_date="2024-02-01", flight_from_id=1),
    Trip(package_id=2, start_date="2024-02-05", end_date="2024-03-01", flight_from_id=2),
    Trip(package_id=3, start_date="2024-03-05", end_date="2024-04-01", flight_from_id=3),
]


def create_packages():
    Country.objects.bulk_create(countries)
    PopularPlace.objects.bulk_create(popular_places)
    PackageFeature.objects.bulk_create(package_features)
    Trip.objects.bulk_create(trips)
    PackagePicture.objects.bulk_create(pictures)
    Destination.objects.bulk_create(destinations)
    Package.objects.bulk_create(packages)
    PlanType.objects.bulk_create(plan_types)
    Plan.objects.bulk_create(plans)
    Package.objects.get(pk=1).popular_places.add(1, 2)
    Package.objects.get(pk=2).popular_places.add(3, 4)
    Package.objects.get(pk=3).popular_places.add(5, 6)
    for package in Package.objects.all():
        package.core_features.add(1, 2, 3)


__all__ = ['create_packages']
