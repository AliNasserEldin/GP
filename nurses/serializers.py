from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *
from rest_framework.response import Response
from patients.models import *


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'number_in_qeue', 'type', 'patient']
        depth = 1        

   ############################# Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields ='__all__'
        depth = 1        



class GetRoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=False)
    def validate(self, data):
        if 'name' not in data :
            raise serializers.ValidationError({"message": "'name' must be provided"})
        return data
    

class BesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields ='__all__'
        depth = 1  


class updateRoomSerializer(serializers.Serializer):
    number_in_room = serializers.CharField(max_length=13, required=False)
    room_status = serializers.IntegerField(required=False)
    # incharge=serializers.CharField(max_length=13, required=False)
    bed_status  =serializers.CharField(max_length=13, required=False)
    disease=serializers.CharField(max_length=13, required=False)
    treatment=serializers.CharField(max_length=13, required=False)
    descrption=serializers.CharField(max_length=13, required=False)
    # patients
    # doctors
    # nurses
    reserved_from=serializers.DateTimeField(required=False)
    reserved_until=serializers.DateTimeField(required=False)

    def validate(self, data):
        if 'room_status' not in data and 'number_in_room' not in data and 'incharge' not in data:
            raise serializers.ValidationError({"message": "At least one of 'number_in_room' or 'room_status' or 'incharge' must be provided"})
        
        if 'room_status' in data and data['room_status'] not in ['Occupied', 'Full','Book','Empty']:
            raise serializers.ValidationError({"room_status": "Invalid status"})
        
        if 'bed_status' in data and data['bed_status'] not in ['Occupied', 'CheckOut','Booked','Empty']:
            raise serializers.ValidationError({"room_status": "Invalid status"})
        
        if 'number_in_room' in data and data['number_in_room'] is not None and data['number_in_room'] <= 3:
            raise serializers.ValidationError({"number_in_room": "Invalid number_in_room max number id{max}"})
        
        if 'treatment' in data and len(data['treatment']) <= 13:
            raise serializers.ValidationError({"treatment": "Invalid treatment be at least 8 characters."}) 
        
        if 'disease' in data and len(data['disease']) <= 13:
            raise serializers.ValidationError({"disease": "Invalid diseasemust be at least 8 characters."})      
          
        if 'descrption' in data and len(data['descrption']) <= 100:
            raise serializers.ValidationError({"descrption": "Invalid descrption be at least 100 characters."})           

        # if 'incharge' in data and data['incharge'] is not None and data['incharge'] is not Employee:
        #     raise serializers.ValidationError({"incharge": "Invalid incharge"})
        return data



###################################  Calls




class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calls
        fields ='__all__'
        depth = 1   





# class PreserveCallSerializer(serializers.Serializer):
#     room_id = serializers.IntegerField()
#     patient_id = serializers.IntegerField()
#     doctor_id = serializers.IntegerField()
#     nurse_id = serializers.IntegerField()

#     def validate(self,data):
        
#         if not Room.objects.filter(id=data['room_id']).exists():
#             raise ValidationError({"room_id": "room does not exist"})
#         if not Employee.objects.filter(id=data['patient_id']).exists():
#             raise ValidationError({"patient_id": "patient does not exist"})
#         if not Employee.objects.filter(id=data['doctor_id']).exists():
#             raise ValidationError({"doctor_id": "doctor does not exist"})
#         if not Employee.objects.filter(id=data['nurse_id']).exists():
#             raise ValidationError({"nurse_id": "nurse does not exist"})
        
#         if data['status'] not in ['Pending', 'Done']:
#             raise ValidationError("Invalid status. Must be Pending, or Done.")
        
#         if data['type'] not in ['Surgery', 'inPatient Treatment']:
#             raise ValidationError("Invalid type. Must be Surgery, or inPatient Treatment.")
        
#         if len(data['room']) < 1:
#             raise ValidationError({"room": "room name must be at least 1 characters."})
#         if len(data['disease']) < 2:
#             raise ValidationError({"disease": "disease name must be at least 2 characters."})
#         if len(data['treatment']) < 2:
#             raise ValidationError({"treatment": "treatment name must be at least 2 characters."})
#         if len(data['descrption']) < 2:
#             raise ValidationError({"descrption": "descrption must be at least 2 characters."})                
#         return data
