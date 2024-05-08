from rest_framework import serializers
#
from .models import Nota

class NotaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ('__all__')