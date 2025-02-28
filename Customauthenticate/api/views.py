from .models import Student
from .serializer import Studentserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.customauth import CustomAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializer
    authentication_classes=[CustomAuthentication]
    permission_classes=[IsAuthenticated]




