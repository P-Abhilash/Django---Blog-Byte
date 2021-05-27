from django import forms
from django.forms import widgets
from django.forms import TextInput,Textarea
from .models import BlogPost

class BlogPostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Title'}),label="Title : ")
    slug = forms.SlugField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Slug'}),label="Slug : ")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write something here...'}),label="Content : ")

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image','slug', 'content', 'publish_date']
        widgets ={
            'title' : TextInput(attrs={'class':'form-control', 'placeholder': 'Title'}),
            'slug' : TextInput(attrs={'class':'form-control', 'placeholder': 'Slug'}),
            'content' : Textarea(attrs={'class':'form-control', 'placeholder': 'Write something here...'}),
            'publish_date' : TextInput(attrs={'class':'form-control', 'placeholder': 'YYYY-MM-DD'})
        }

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact = title)
        if instance is not None:
            qs = qs.exclude(pk = instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has already exist. Please try another one")
        return title