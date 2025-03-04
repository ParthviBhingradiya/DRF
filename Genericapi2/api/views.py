#GenericAPIView and Model Mixin

from .models import Student
from .serializer import Studentserializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    # convert data json formate
    serializer_class=Studentserializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
    
class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    # convert data json formate
    serializer_class=Studentserializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args,**kwargs)