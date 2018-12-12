from django import forms
from word.models import Word

class PostForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('word_spell', 'word_mean',)

