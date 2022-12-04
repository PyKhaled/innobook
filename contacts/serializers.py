from rest_framework import serializers
from contacts.models import Contact, Number
from django.db import Error, transaction

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ('label', 'dial')


class ContactSerializer(serializers.ModelSerializer):
    numbers = NumberSerializer(many=True)
    
    class Meta:
        model = Contact
        fields = "__all__"

    def create(self, validated_data):
        numbers_input = validated_data.pop('numbers')
        try:
            with transaction.atomic():
                contact = Contact.objects.create(**validated_data)
                for number in numbers_input:
                    Number.objects.create(contact=contact, **number)
            return contact
        except Exception as e:
            print(e)
        print('done')