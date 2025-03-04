from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
# from .mypagination import MyPageNumberPagination
# set limit of page size
from .mypagination import LimitOffsetPagination

# cursor pagination
from .mypagination import MyCursorPagination


# Create your views here.

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = MyPageNumberPagination 
    # set limit of page size
    # pagination_class = LimitOffsetPagination

    # cursor pagination
    pagination_class = MyCursorPagination


