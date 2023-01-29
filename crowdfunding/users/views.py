from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer

class CustomUserList(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomUserDetail(APIView):
    def get_object(self,pk):
        try: 
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user =self.get_object(pk)
        data = request.data
        
        serializer = CustomUserSerializer(instance=user, data=data, partial=True)
        
        
class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (IsAuthenticated,)

    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data, instance=user)

        if serializer.is_valid():
            # # Check old password
            # if not self.object.check_password(serializer.data.get("old_password")):
            #     return Response({"Wrong password. Please try again"}, status=status.HTTP_400_BAD_REQUEST)

            # # set_password also hashes the password that the user will get
            # self.object.set_password(serializer.data.get("new_password"))
            # self.object.save()
            # response = {
            #     'status': 'success',
            #     'code': status.HTTP_200_OK,
            #     'message': 'Password updated successfully',
            #     'data': []
            # }
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)