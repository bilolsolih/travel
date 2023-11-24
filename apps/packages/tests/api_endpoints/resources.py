from django.utils import timezone

from apps.base.models import Country, City, Region
from apps.packages.models import PackageFeature, Day, AccommodationType, AccommodationFeature, PackagePicture, Destination, AccommodationPicture, Trip, Accommodation, Package
from apps.places.models import PopularPlace

countries = [
    Country(title='Egypt'),
    Country(title='Pakistan'),
    Country(title='United Arab Emirates'),
    Country(title='Saudi Arabia'),
]

cities = [
    City(country_id=1, title='City 1'),
    City(country_id=2, title='City 2'),
    City(country_id=3, title='City 3'),
    City(country_id=4, title='City 4'),
]

regions = [
    Region(title='Namangan'),
    Region(title='Andijon'),
    Region(title='Farg\'ona'),
]

popular_places = [
    PopularPlace(title='Popular place 1', picture='test_data/hotel.jpg', description='Description 1'),
    PopularPlace(title='Popular place 2', picture='test_data/motel.jpg', description='Description 2'),
    PopularPlace(title='Popular place 3', picture='test_data/villas.jpg', description='Description 3'),
    PopularPlace(title='Popular place 4', picture='test_data/accommodation_1.jpg', description='Description 4'),
    PopularPlace(title='Popular place 5', picture='test_data/accommodation_2.jpg', description='Description 5'),
    PopularPlace(title='Popular place 6', picture='test_data/accommodation_3.jpg', description='Description 6'),
]

features = [
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

pictures = [
    PackagePicture(package_id=1, picture='test_data/package_1', is_main=True),
    PackagePicture(package_id=1, picture='test_data/package_2'),
    PackagePicture(package_id=2, picture='test_data/package_3', is_main=True),
    PackagePicture(package_id=2, picture='test_data/package_4'),
]

destinations = [
    Destination(package_id=1, city_id=1, duration=5),
    Destination(package_id=1, city_id=2, duration=5),
    Destination(package_id=2, city_id=3, duration=5),
    Destination(package_id=2, city_id=4, duration=5),
]

days = [
    Day(package_id=1, day_number=1),
    Day(package_id=1, day_number=2),
    Day(package_id=2, day_number=1),
    Day(package_id=2, day_number=2),
]

date = timezone.now().date()
trips = [
    Trip(package_id=1, start_date=date, flight_from_id=1),
    Trip(package_id=2, start_date=date, flight_from_id=2),
]

# ACCOMMODATIONS
accommodation_features = [
    AccommodationFeature(title='Feature 1', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=False),
    AccommodationFeature(title='Feature 2', icon='test_data/icon.jpg', description='Description', is_popular=True, is_paid=False),
    AccommodationFeature(title='Feature 3', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=True),
    AccommodationFeature(title='Feature 4', icon='test_data/icon.jpg', description='Description', is_popular=True, is_paid=True),
    AccommodationFeature(title='Feature 5', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=False),
    AccommodationFeature(title='Feature 6', icon='test_data/icon.jpg', description='Description', is_popular=True, is_paid=False),
    AccommodationFeature(title='Feature 7', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=True),
    AccommodationFeature(title='Feature 8', icon='test_data/icon.jpg', description='Description', is_popular=True, is_paid=True),
]

accommodation_types = [
    AccommodationType(title='Hotel', picture='test_data/hotel.jpg'),
    AccommodationType(title='Motel', picture='test_data/motel.jpg'),
    AccommodationType(title='Villa', picture='test_data/villas.jpg'),
]
accommodation_pictures = [
    AccommodationPicture(accommodation_id=1, picture='test_data/accommodation_1.jpg', is_main=True),
    AccommodationPicture(accommodation_id=1, picture='test_data/accommodation_2.jpg'),
    AccommodationPicture(accommodation_id=1, picture='test_data/accommodation_3.jpg'),
    AccommodationPicture(accommodation_id=1, picture='test_data/accommodation_4.jpg'),

    AccommodationPicture(accommodation_id=2, picture='test_data/accommodation_1.jpg'),
    AccommodationPicture(accommodation_id=2, picture='test_data/accommodation_2.jpg', is_main=True),
    AccommodationPicture(accommodation_id=2, picture='test_data/accommodation_3.jpg'),
    AccommodationPicture(accommodation_id=2, picture='test_data/accommodation_4.jpg'),

    AccommodationPicture(accommodation_id=3, picture='test_data/accommodation_1.jpg'),
    AccommodationPicture(accommodation_id=3, picture='test_data/accommodation_2.jpg'),
    AccommodationPicture(accommodation_id=3, picture='test_data/accommodation_3.jpg', is_main=True),
    AccommodationPicture(accommodation_id=3, picture='test_data/accommodation_4.jpg'),

    AccommodationPicture(accommodation_id=4, picture='test_data/accommodation_1.jpg'),
    AccommodationPicture(accommodation_id=4, picture='test_data/accommodation_2.jpg'),
    AccommodationPicture(accommodation_id=4, picture='test_data/accommodation_3.jpg'),
    AccommodationPicture(accommodation_id=4, picture='test_data/accommodation_4.jpg', is_main=True),
]


def create_packages():
    Country.objects.bulk_create(countries)
    City.objects.bulk_create(cities)
    Region.objects.bulk_create(regions)
    PopularPlace.objects.bulk_create(popular_places)
    PackageFeature.objects.bulk_create(features)
    Day.objects.bulk_create(days)
    Trip.objects.bulk_create(trips)
    PackagePicture.objects.bulk_create(pictures)
    Destination.objects.bulk_create(destinations)

    package_1 = Package(title='Package 1', description='Description 1', country_id=1)
    package_2 = Package(title='Package 2', description='Description 2', country_id=1)

    Package.objects.bulk_create([
        package_1,
        package_2,
    ])
    package_1.popular_places.add(1)
    package_1.core_features.add(1)


def create_accommodations():
    accommodation_1 = Accommodation(title='Title 1', type_id=1, short_description='Short', long_description='Long', rating=5, city_id=1, address='address', landmark='landmark')
    accommodation_2 = Accommodation(title='Title 2', type_id=2, short_description='Short', long_description='Long', rating=4, city_id=2, address='address', landmark='landmark')
    accommodation_3 = Accommodation(title='Title 3', type_id=3, short_description='Short', long_description='Long', rating=3, city_id=3, address='address', landmark='landmark')
    accommodation_4 = Accommodation(title='Title 4', type_id=2, short_description='Short', long_description='Long', rating=2, city_id=4, address='address', landmark='landmark')

    accommodations = [
        accommodation_1,
        accommodation_2,
        accommodation_3,
        accommodation_4,
    ]

    AccommodationFeature.objects.bulk_create(accommodation_features)
    AccommodationType.objects.bulk_create(accommodation_types)
    Accommodation.objects.bulk_create(accommodations)
    AccommodationPicture.objects.bulk_create(accommodation_pictures)

    for accommodation in accommodations:
        accommodation.features.add(1, 2, 3, 4, 5, 6, 7, 8)


__all__ = [
    'create_accommodations', 'create_packages'
]
