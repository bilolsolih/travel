from apps.about.models import PhoneNumber

phone_numbers = [
    PhoneNumber(phone_number="+998902958899", is_active=True),
    PhoneNumber(phone_number="+998912958899", is_active=False),
    PhoneNumber(phone_number="+998922958899", is_active=False),
]


def create_phone_number():
    PhoneNumber.objects.bulk_create(phone_numbers)


__all__ = ['create_phone_number']
