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
            'nota',
            'ativo'
        )


class MateriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materia
        fields = (
            'id',
            'materia',
            'url',
            'ativo'
         )
