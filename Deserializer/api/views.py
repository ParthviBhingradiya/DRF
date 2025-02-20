from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def Student_create(request):
    if request.method=='POST':
        json_data=request.body
        #covert json data byte stream
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Inserted'}
            json_data=JSONRenderer().render(res)
            return JsonResponse(serializer.data)
        json_data=JSONRenderer().render(serializer.errors)
        return JsonResponse(serializer.data)
