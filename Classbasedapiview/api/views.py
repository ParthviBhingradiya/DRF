from django.shortcuts import render
from .models import Student
from rest_framework.response import Response
from .serializer import Studentserializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class StudentAPI(APIView):
    def get(self,request,formate=None,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=Studentserializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=Studentserializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request,formate=None):
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,formate=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=Studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complate Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,formate=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=Studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,formate=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_201_CREATED)