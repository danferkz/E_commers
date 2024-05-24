from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import Users
from user.api.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserList(APIView):
    try:
        def get(self, request):
            users = Users.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(str(e))
        
class UserUpdate(APIView):
    try:
        permission_classes = [IsAuthenticated]
        authentication_classes = [TokenAuthentication]
        def get(self, request, pk):
            user = Users.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        def put(self, request, pk):
            user = Users.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        def delete(self, request, pk):
            user = Users.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(str(e))
        
