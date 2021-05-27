from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write something here...'}))

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email.endswith(".edu"):
            raise forms.ValidationError("This is not a valid email, please don't use .edu")
        return email