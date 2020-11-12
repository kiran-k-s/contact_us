
from rest_framework import serializers
from home.models import Contactus

class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contactus
        fields = ('id', 'name', 'email', 'phone', 'description')

        
    