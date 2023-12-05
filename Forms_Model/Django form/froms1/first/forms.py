from typing import Any
from django import forms
from django.core import validators

class contactform(forms.Form):
    # # # # 1
    # name = forms.CharField(label='User Name')
    # email = forms.EmailField(label='User Email')
    
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # Balance = forms.DecimalField()
    
    # check = forms.BooleanField()
    
    # Birthday = forms.DateField()
    # BirthTime = forms.DateTimeField()
    
    # CHOICE = [('s', 'small'), ('m', 'Midum'), ('l', 'Large')]
    # size = forms.ChoiceField(choices=CHOICE)
    # LANGUAGE = [('p', 'Python'), ('c', 'C'), ('j', 'Java'), ('js', 'Javascript')]
    # Language = forms.MultipleChoiceField(choices=LANGUAGE)
    
    
    # # imge ba file upload ar jonne form.html a 
    # # form tag ar modde
        # # <form enctype = 'multipart/form-data' >
        
    # File = forms.FileField()
    # image = forms.ImageField()
    
    # # # # 2
    
    # name = forms.CharField(label='User Name', initial='Rahim', help_text='Total length must be 20 char', required=False)
    # required by default true, disabled = false
    # email = forms.EmailField(label='User Email')
    
    # # # # 3
    # ########
    # widgets == field to html input
    # we can change forms type use widgets
    # html ar forms ar sokol kaj amra widgets use kore python diye korte pari.
    # widget=forms.Textarea(attrs = {'id': 'temp, 'class':'class1 class2', 'placeholder': 'enter your name'})
    # #########
    # name = forms.CharField(label='User Name', widget=forms.Textarea(attrs={'placeholder': 'Enter your name'}))
    
    # Birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # Birthtime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    
    # CHOICE = [('s', 'small'), ('m', 'Midum'), ('l', 'Large')]
    # size = forms.ChoiceField(choices=CHOICE, widget=forms.RadioSelect)
    
    # LANGUAGE = [('p', 'Python'), ('c', 'C'), ('j', 'Java'), ('js', 'Javascript')]
    # Language = forms.MultipleChoiceField(choices=LANGUAGE, widget=forms.CheckboxSelectMultiple)
    
    
    # # # # 4
    ##########################################
    # # # # validation
    #########################################
    
    # name = forms.CharField(widget=forms.TextInput)
    # email = forms.EmailField(widget=forms.EmailInput)
    # # # custom validation
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter a name atlast 10 character') 
    #     return valname
    
    # def clean_email(self):
    #     mailname = self.cleaned_data['email']
    #     if 'gamil' not in mailname or '.com' not in mailname:
    #         raise forms.ValidationError('Enter a valid email account')
    #     return mailname
    
    # # one function all validation
    
    # def clean(self):
    #     cleaned_data =  super().clean()
        
    #     valname= self.cleaned_data['name']
    #     valemail= self.cleaned_data['email']
        
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter a name atlast 10 character') 
        
    #     if 'gmail' not in valemail or '.com' not in valemail:
    #         raise forms.ValidationError('Enter a valid email account')
    
    # # # # 5
    #######################
    # # # Builtin Form Validators
    ################################
    # # import
        # # from django.core import validators
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name atlast 10 character')])
    
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])
    
    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(50, message='under 50'), validators.MinValueValidator(18, message='age must 18+')])
    
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf',])])