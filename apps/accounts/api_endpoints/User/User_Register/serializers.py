from rest_framework import serializers

from apps.accounts.models import User, VerifiedPhoneNumber


class UserRegisterSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'region', 'profile_photo']

    def validate(self, attrs):
        if not VerifiedPhoneNumber.objects.filter(phone_number=attrs['phone_number'], device_id=attrs['device_id']).exists():
            raise serializers.ValidationError({'phone_number': 'Phone number is not verified.'})
        super().validate(attrs)

    def create(self, validated_data):
        VerifiedPhoneNumber.objects.filter(phone_number=validated_data['phone_number']).delete()
        return self.Meta.model.objects.create_user(**validated_data)
