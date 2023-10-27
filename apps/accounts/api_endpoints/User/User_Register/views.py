from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response

from .permissions import IsNotAuthenticated
from .serializers import UserRegisterSerializer


class UserRegisterAPIView(CreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        return serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token = RefreshToken.for_user(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        headers = self.get_success_headers(serializer.data)
        return Response({'refresh': refresh_token, 'access': access_token}, status=status.HTTP_201_CREATED, headers=headers)
        
        
    


__all__ = ['UserRegisterAPIView']
from rest_framework_simplejwt.tokens import RefreshToken
from apps.accounts.models import User, OTPCode


class UserTokenObtainSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    code = serializers.CharField(max_length=4)

    def validate(self, attrs):
        try:
            user = User.objects.get(phone_number=attrs['phone_number'])
            exist = True
        except User.DoesNotExist:
            exist = False
        #
        #     try:
        #         OTPCode.objects.get(user=user, code=attrs['code'], is_expired=False)
        #     except OTPCode.DoesNotExist:
        #         raise serializers.ValidationError({'code': 'Code for this user does not exist.'})
        if attrs['code'] != '1111':
            raise serializers.Validatio
