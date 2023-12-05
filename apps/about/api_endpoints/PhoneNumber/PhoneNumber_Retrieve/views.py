from rest_framework.generics import RetrieveAPIView

from apps.about.models import PhoneNumber
from .serializers import PhoneNumberRetrieveSerializer


class PhoneNumberRetrieveAPIView(RetrieveAPIView):
    serializer_class = PhoneNumberRetrieveSerializer

    def get_object(self):
        return PhoneNumber.objects.filter(is_active=True).first()


__all__ = ['PhoneNumberRetrieveAPIView']
