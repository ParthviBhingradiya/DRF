from .models import Student
from .serializer import Studentserializer
from rest_framework import viewsets

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=Studentserializer

# StudentReadOnlyModelViewSet
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializer

