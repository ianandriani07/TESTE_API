from rest_framework import serializers

from .models import Materia, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'materia',
            'nome',
            'email',
            'feedback',
            'ativo',
            'nota'
        )

class MateriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materia
        fields = (
            'id',
            'materia',
            'ativo'
         )
