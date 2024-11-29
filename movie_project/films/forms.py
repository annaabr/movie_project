from .models import Films_info
from django.forms import ModelForm, Textarea, TextInput

class Films_info_form(ModelForm):
    class Meta:
        model = Films_info
        fields = ['title', 'description', 'feedback']
        widgets ={
            'title': TextInput(attrs={'class': "form-control", 'placeholder': "Введите название фильма"}),
            'description': Textarea(attrs={'class': "form-control", 'placeholder': "Введите описание фильма"}),
            'feedback': Textarea(attrs={'class': "form-control", 'placeholder': "Введите отзыв на фильм"})
        }
