from apps.base.models import City, Region
from apps.packages.models import Day, Activity, ActivityBridge, ActivityPicture, Stay, Flight

days = [
    Day(package_id=1, day_number=1),
    Day(package_id=1, day_number=2),
    Day(package_id=1, day_number=3),
    Day(package_id=2, day_number=1),
    Day(package_id=2, day_number=2),
    Day(package_id=2, day_number=3),
    Day(package_id=3, day_number=1),
    Day(package_id=3, day_number=2),
    Day(package_id=3, day_number=3),
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

flights = [
    Flight(day_id=1, from_city_id=1, to_city_id=2, due_time='08:00:00'),
    Flight(day_id=3, from_city_id=2, to_city_id=1, due_time='08:00:00'),
    Flight(day_id=4, from_city_id=2, to_city_id=3, due_time='08:00:00'),
    Flight(day_id=6, from_city_id=3, to_city_id=2, due_time='08:00:00'),
    Flight(day_id=7, from_city_id=3, to_city_id=4, due_time='08:00:00'),
    Flight(day_id=9, from_city_id=4, to_city_id=3, due_time='08:00:00'),
]

stays = [
    Stay(day_id=1, accommodation_id=1, due_time='12:00:00'),
    Stay(day_id=4, accommodation_id=2, due_time='12:00:00'),
    Stay(day_id=7, accommodation_id=3, due_time='12:00:00'),
]

activities = [
    Activity(title='Title 1', address='test', landmark='test', description='test', iframe='test', latitude='123', longitude='123'),
    Activity(title='Title 2', address='test', landmark='test', description='test', iframe='test', latitude='123', longitude='123'),
    Activity(title='Title 3', address='test', landmark='test', description='test', iframe='test', latitude='123', longitude='123'),
]

activity_pictures = [
    ActivityPicture(activity_id=1, picture='test_data/icon.jpg', is_main=True),
    ActivityPicture(activity_id=1, picture='test_data/icon.jpg', is_main=False),
    ActivityPicture(activity_id=2, picture='test_data/icon.jpg', is_main=False),
    ActivityPicture(activity_id=2, picture='test_data/icon.jpg', is_main=False),
    ActivityPicture(activity_id=3, picture='test_data/icon.jpg', is_main=True),
    ActivityPicture(activity_id=3, picture='test_data/icon.jpg', is_main=False),
]

activity_bridges = [
    ActivityBridge(day_id=1, plan_id=1, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=1, plan_id=2, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=1, plan_id=3, activity_id=3, due_time='15:00:00'),
    ActivityBridge(day_id=2, plan_id=1, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=2, plan_id=2, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=2, plan_id=3, activity_id=3, due_time='15:00:00'),
    ActivityBridge(day_id=3, plan_id=1, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=3, plan_id=2, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=3, plan_id=3, activity_id=3, due_time='15:00:00'),
    ActivityBridge(day_id=4, plan_id=4, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=4, plan_id=5, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=4, plan_id=6, activity_id=3, due_time='15:00:00'),
    ActivityBridge(day_id=5, plan_id=4, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=5, plan_id=5, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=5, plan_id=6, activity_id=3, due_time='15:00:00'),
    ActivityBridge(day_id=6, plan_id=4, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=6, plan_id=5, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=6, plan_id=6, activity_id=3, due_time='15:00:00'),
    ActivityBridge(day_id=7, plan_id=7, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=7, plan_id=8, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=7, plan_id=9, activity_id=3, due_time='15:00:00'),
    ActivityBridge(day_id=8, plan_id=7, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=8, plan_id=8, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=8, plan_id=9, activity_id=3, due_time='15:00:00'),
    ActivityBridge(day_id=9, plan_id=7, activity_id=1, due_time='13:00:00'),
    ActivityBridge(day_id=9, plan_id=8, activity_id=2, due_time='14:00:00'),
    ActivityBridge(day_id=9, plan_id=9, activity_id=3, due_time='15:00:00'),
]


def create_days():
    City.objects.bulk_create(cities)
    Region.objects.bulk_create(regions)
    Day.objects.bulk_create(days)
    Flight.objects.bulk_create(flights)
    Stay.objects.bulk_create(stays)
    Activity.objects.bulk_create(activities)
    ActivityPicture.objects.bulk_create(activity_pictures)
    ActivityBridge.objects.bulk_create(activity_bridges)


__all__ = ['create_days']
