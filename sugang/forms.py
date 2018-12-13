from django import forms
from .models import Subject, Take, Instructor


class ClassForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['sub_categorize', 'sub_name', 'i_name', 'total_lecture', 'lecture_level', 'book']


class TakeForm(forms.ModelForm):
    class Meta:
        model = Take
        fields = ['username', 'subject']


class SignForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'i_id', 'i_pw']

