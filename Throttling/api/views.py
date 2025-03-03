from .models import Student
from .serializer import Studentserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api.Throttling import JackRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    # any one user define request
    # throttle_classes=[AnonRateThrottle,JackRateThrottle]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]





