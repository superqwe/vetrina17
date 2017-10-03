from django.db import models


class Tipo(models.Model):
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipi"

    def __str__(self):
        return '%s' % self.tipo

    tipo = models.CharField(max_length=50)


class Creazione(models.Model):
    class Meta:
        verbose_name = "Collezione"
        verbose_name_plural = "Collezioni"

    def __str__(self):
        return '%s' % self.nome

    tipo = models.ForeignKey(Tipo)
    anno = models.IntegerField()
    nome = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='./static/vetrina/img/creazioni')
    descrizione = models.TextField()

