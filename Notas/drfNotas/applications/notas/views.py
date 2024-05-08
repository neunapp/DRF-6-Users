from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import(
    ListAPIView
)
#
from .models import Nota
from .serializers import NotaSerilizer


class SoloMasculino(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.user.gender == 'M':
            return True
        else:
            return False

class ListaNotas(ListAPIView):
    serializer_class = NotaSerilizer
    queryset = Nota.objects.all()
    permission_classes = [IsAuthenticated, SoloMasculino]
    authentication_classes = [TokenAuthentication,]

