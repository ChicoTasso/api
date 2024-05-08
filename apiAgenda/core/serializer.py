from .models import *
from rest_framework import serializers

class AgendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agenda
        fields = ('nome', 'telefone', 'email')