from rest_framework import serializers
from .models import Address, Person, Account


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class AccountStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'



