from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse,JsonResponse

# Create your views here.

def student_details(request):

    #complex data
    stu=Student.objects.get(id=1)
    print('stu: ', stu)

    #python data
    serializer=StudentSerializer(stu)
    print('serializer: ', serializer)
    print('serializer: ', serializer.data)

    #json data
    # json_data=JSONRenderer().render(serializer.data)
    # print('json_data: ', json_data)
    # return HttpResponse(json_data , content_type='application/json')
    
    #use jsonresponse
    return JsonResponse(serializer.data)