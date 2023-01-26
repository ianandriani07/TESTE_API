from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    MateriaAPIView,
    AvaliacaoAPIView,
    MateriasAPIView,
    AvaliacoesAPIView,
    MateriaViewSet,
    AvaliacaoViewSet
)

router = SimpleRouter()
router.register('materias', MateriaViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('materias/', MateriasAPIView.as_view(), name='materias'),
    path('materias/<int:pk>', MateriaAPIView.as_view(), name='materia'),
    path('materias/<int:materia_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='materia_avaliacoes'),
    path('materias/<int:materia_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(),
         name='materia_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='avaliacao')
]
