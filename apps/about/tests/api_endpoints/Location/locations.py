from random import randint  # noqa

from apps.about.models import Location
from apps.base.models import Region

regions = [
    Region(title='Namangan'),
    Region(title='Andijon'),
    Region(title='Farg\'ona'),
]

locations = [
    Location(title='Title 1', region_id=1, city='City 1', iframe='iframe 1', latitude='1', longitude='1'),
    Location(title='Title 2', region_id=2, city='City 2', iframe='iframe 2', latitude='2', longitude='2'),
    Location(title='Title 3', region_id=3, city='City 3', iframe='iframe 3', latitude='3', longitude='3'),
]


def create_locations():
    Region.objects.bulk_create(regions)
    Location.objects.bulk_create(locations)


__all__ = ['create_locations']
