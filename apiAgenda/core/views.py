from .models import Agenda
from rest_framework import viewsets, status
from .serializer import AgendaSerializer
from rest_framework.response import Response

# Create your views here.

class AgendaViewSet(viewsets.ViewSet):
    
    def listar(self, request):
        agendas = Agenda.objects.all()
        serializer = AgendaSerializer(agendas, many=True)
        return Response(serializer.data)
    
    def ler(self, request, pk):
        agenda = Agenda.objects.get(pk=pk)
        serializer = AgendaSerializer(agenda)
        return Response(serializer.data)
    
    def criar(self, request):
        serializer = AgendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def atualizar(self, request, pk):

        agenda = Agenda.objects.get(pk=pk)
        serializer = AgendaSerializer(agenda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def excluir(self, request, pk):

        agenda = Agenda.objects.get(pk=pk)
        agenda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    