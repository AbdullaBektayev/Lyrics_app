from django.forms import ModelForm,TextInput
from .models import Song

class SongForm(ModelForm): # creating from for database Song
    class Meta:
        model = Song
        fields = ['artist','title']
        widgets = {
            'artist' : TextInput(attrs={ # html input with parameters
                'class': 'form-control',
                'name': 'artist',
                'id': 'artist',
                'placeholder': 'Input The Artist'
            }),
            'title': TextInput(attrs={ # html input with parameters
                'class': 'form-control',
                'name': 'title',
                'id': 'title',
                'placeholder': 'Input The Song'
            })
        }
