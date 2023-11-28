from apps.packages.models import AccommodationType, AccommodationFeature, AccommodationPicture, Accommodation

accommodation_features = [
    AccommodationFeature(title='Feature 1', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=False),
    AccommodationFeature(title='Feature 2', icon='test_data/icon.jpg', description='Description', is_popular=True, is_paid=False),
    AccommodationFeature(title='Feature 3', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=True),
    AccommodationFeature(title='Feature 4', icon='test_data/icon.jpg', description='Description', is_popular=True, is_paid=True),
    AccommodationFeature(title='Feature 5', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=False),
    AccommodationFeature(title='Feature 6', icon='test_data/icon.jpg', description='Description', is_popular=True, is_paid=False),
    AccommodationFeature(title='Feature 7', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=True),
    AccommodationFeature(title='Feature 8', icon='test_data/icon.jpg', description='Description', is_popular=True, is_paid=True),
    AccommodationFeature(title='Feature 9', icon='test_data/icon.jpg', description='Description', is_popular=False, is_paid=True),
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
]

accommodations = [
    Accommodation(title='Title 1', type_id=1, short_description='Short', long_description='Long', rating=5, city_id=1, address='address', landmark='landmark'),
    Accommodation(title='Title 2', type_id=2, short_description='Short', long_description='Long', rating=4, city_id=2, address='address', landmark='landmark'),
    Accommodation(title='Title 3', type_id=3, short_description='Short', long_description='Long', rating=3, city_id=3, address='address', landmark='landmark'),
]


def create_accommodations():
    Accommodation.objects.bulk_create(accommodations)
    AccommodationFeature.objects.bulk_create(accommodation_features)
    AccommodationType.objects.bulk_create(accommodation_types)
    AccommodationPicture.objects.bulk_create(accommodation_pictures)

    for accommodation in Accommodation.objects.all():
        accommodation.features.add(1, 2, 3, 4, 5, 6, 7, 8, 9)


__all__ = ['create_accommodations']
