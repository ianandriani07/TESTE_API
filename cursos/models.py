from django.db import models


class Base(models.Model):
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Materia(Base):
    materia = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'

    def __str__(self):
        return self.materia


class Avaliacao(Base):

    materia = models.ForeignKey(Materia, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField(blank=True, default='')
    nota = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'materia']

    def __str__(self):
        return '{} tirou {} na matéria de {}'.format(self.nome, self.nota, self.materia)
