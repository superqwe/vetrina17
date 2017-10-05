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


class Evento(models.Model):
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"

    def __str__(self):
        return '%s' % self.nome

    nome = models.CharField(max_length=100)
    luogo = models.CharField(max_length=200)
    dal = models.DateField()
    al = models.DateField()
    descrizione = models.TextField()
    link = models.URLField()


class Messaggio(models.Model):
    class Meta:
        verbose_name = "Messaggio"
        verbose_name_plural = "Messaggi"

    def __str__(self):
        return '%s -- %s' % (self.nome, self.data)

    nome = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    messaggio = models.TextField()
