from django import forms
from .models import GigReview, Profile, Artist, Venue
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from django.contrib.auth.password_validation import get_default_password_validators


class GigReviewForm(forms.ModelForm):
    class Meta:
        model = GigReview
        fields = ['artist', 'venue', 'gig_date', 'title', 'image', 'review']
        widgets = {
            'gig_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gig_date'].input_formats = ['%Y-%m-%d']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'facebook', 'instagram', 'image']


class FanContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class ArtistContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    logo = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)


class VenueContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    logo = forms.ImageField(required=False)
    town = forms.CharField(max_length=100)
    post_code = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)


class SearchForm(forms.Form):
    SEARCH_TYPE_CHOICES = [
        ('artist', 'Artist'),
        ('venue', 'Venue'),
    ]
    search_type = forms.ChoiceField(choices=SEARCH_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    search_term = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search by name...'}))


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2")
