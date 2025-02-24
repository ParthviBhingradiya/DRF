from .models import Student
from .serializer import Studentserializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserializer