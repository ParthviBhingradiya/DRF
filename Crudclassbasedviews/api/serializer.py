from rest_framework import serializers
from .models import Student

#validator
def staet_with_r(value):
        if value[0].lower()!='t':
            raise serializers.ValidationError("Name should be start with t")

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,validators=[staet_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    #field level validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat Full!")
        return value
    
    #object level validation
    def validate(self,data):
        nm=data.get('name')
        city=data.get('city')
        if nm.lower()=='test' and city.lower()!='surat':
            raise serializers.ValidationError("City must be Surat")
        return data
 
