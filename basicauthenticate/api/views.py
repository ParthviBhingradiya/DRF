from .models import Student
from .serializer import Studentserializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[AllowAny]




