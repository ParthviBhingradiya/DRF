from .models import Student
from .serializer import Studentserializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from .custompermission import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]
    # permission_classes=IsAdminUser
    # permission_classes=IsAuthenticatedOrReadOnly
    permission_classes=[MyPermission]





