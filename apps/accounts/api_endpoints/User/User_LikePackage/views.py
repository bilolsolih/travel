from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserLikePackageSerializer


class UserLikeDislikePackageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=UserLikePackageSerializer)
    def post(self, request, *args, **kwargs):
        serializer = UserLikePackageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        package = serializer.validated_data['package']
        if request.user.liked_packages.contains(package):
            request.user.liked_packages.remove(package)
            message = 'Successfully disliked.'
        else:
            request.user.liked_packages.add(package)
            message = 'Successfully liked.'
        return Response({'detail': message}, status=status.HTTP_200_OK)


__all__ = ['UserLikeDislikePackageAPIView']
