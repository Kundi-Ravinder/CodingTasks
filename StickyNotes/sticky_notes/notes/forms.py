from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title',
                'description',
                'is_complete',
                'created_by']