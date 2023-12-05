from random import randint  # noqa

from apps.places.models import PopularPlace

popular_places = [
    PopularPlace(title='Popular place 1', picture='test_data/hotel.jpg', description='Description 1'),
    PopularPlace(title='Popular place 2', picture='test_data/motel.jpg', description='Description 2'),
    PopularPlace(title='Popular place 3', picture='test_data/villas.jpg', description='Description 3'),
    PopularPlace(title='Popular place 4', picture='test_data/accommodation_1.jpg', description='Description 4'),
    PopularPlace(title='Popular place 5', picture='test_data/accommodation_2.jpg', description='Description 5'),
    PopularPlace(title='Popular place 6', picture='test_data/accommodation_3.jpg', description='Description 6'),
]


def create_places():
    PopularPlace.objects.bulk_create(popular_places)


__all__ = ['create_places']
