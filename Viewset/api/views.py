from django.shortcuts import render
from .models import Student
from .serializer import Studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)

        stu=Student.objects.all()
        serializer=Studentserializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=Studentserializer(stu)
            return Response(serializer.data)
    
    def create(self,request):
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)

        serializer=Studentserializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({'msg':'Data Created..'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def update(self,request,pk):
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=Studentserializer(stu,data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({'msg':'Complated Data Updated..'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self,request,pk):
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=Studentserializer(stu,data=request.data,partial=True)
        if serializer.is_valid:
            serializer.save()
            return Response({'msg':'Partial Data Updated..'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk):
        print("Basename:",self.basename)
        print("Action:",self.action)
        print("Detail:",self.detail)
        print("Suffix:",self.suffix)
        print("Name:",self.name)
        print("Description:",self.description)
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted..'},status=status.HTTP_201_CREATED)
    
