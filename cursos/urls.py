from django.urls import path

from .views import MateriaAPIView, AvaliacaoAPIView

urlpatterns = [
    path('materias/', MateriaAPIView.as_view(), name='materias'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
]