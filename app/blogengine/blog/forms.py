from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        """Custom clean method for slug field"""
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == "create":
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            """return object QUERY SET"""
            raise ValidationError(f'Slug must be uniq. We have "{new_slug}" already')

        return new_slug


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        """Custom clean method for slug field"""
        new_slug = self.cleaned_data.get('slug').lower()

        if new_slug == "create":
            raise ValidationError('Slug may not be "Create"')
        return new_slug
