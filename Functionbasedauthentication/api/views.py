from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from .serializer import Studentserializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BaseAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):
    if request.method=='GET':
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=Studentserializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=Studentserializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=='PUT':
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=Studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complate Data Updated'})
        return Response(serializer.errors)
    
    if request.method=='PATCH':
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=Studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
        
    if request.method=='DELETE':
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})