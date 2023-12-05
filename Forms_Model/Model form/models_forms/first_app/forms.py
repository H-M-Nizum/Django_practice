from django import forms
from first_app.models import studentmodel

class studentForm(forms.ModelForm):
    class Meta:
        model = studentmodel
        
        fields = '__all__'
        
        labels = {
            'name': 'student name',
            'roll': 'Class roll',
            'address': 'Home Town',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'})
        }
        
        help_texts = {
            'name': 'Write your full name'
        }
        
        error_messages = {
            'name': {'required': 'Your name is requerd'}
        }