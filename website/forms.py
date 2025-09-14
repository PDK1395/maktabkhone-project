from django import forms
from website.models import Contact , NewsLetter

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()                                    # alan in bimasrafe va tanha bara yadgiri ya rah dovom bood
    subject = forms.CharField(max_length=255)             
    message = forms.CharField(widget=forms.Textarea)
    
    
class ContactForm(forms.ModelForm):
    # last_name = forms.CharField(max_length=255)       inam be in shekl form jadid ezaf mikonim
    subject = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Optional'}))
    class Meta:
        model = Contact
        # fields = ['name','email']    inam be in ravesh to chand marhale az karbar begirim etelayat ro va check konim ke doroste ya na
        fields = '__all__'

        
class Newsletterform(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = '__all__'
        
        
        


