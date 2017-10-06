from django.forms import ModelForm
from .models import Messaggio



class MessaggioForm(ModelForm):
    class Meta:
        model = Messaggio
        fields = ['nome', 'email', 'messaggio']


