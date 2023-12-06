from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    # AuthorForm class ar extra kichu characteristics add korar jonne meta class use kori.
    class Meta:
        model = Author
        
        # specific vabe bolew dite pari kon kon fields thakbe
        # fields = ['name', 'age' .....]
        # ANd caile ataw bolte pari konta thakbe na
        # exclude = ['money'...]
        # all mane sokol fields rakhte caschi form a
        fields = '__all__'