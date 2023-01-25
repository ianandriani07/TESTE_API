from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Materia, Avaliacao
from .serializers import AvaliacaoSerializer, MateriaSerializer

class MateriaAPIView(APIView):

    def get(self, request):
        materias = Materia.objects.all()
        serializer = MateriaSerializer(materias, many=True)
        return Response(serializer.data)

class AvaliacaoAPIView(APIView):

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)