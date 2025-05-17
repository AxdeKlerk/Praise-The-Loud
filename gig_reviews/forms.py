from django import forms
from .models import GigReview, Profile, Artist, Venue

class GigReviewForm(forms.ModelForm):
    class Meta:
        model = GigReview
        # only include the fields you want the user to fill in
        fields = [
            'artist',
            'venue',
            'gig_date',
            'title',
            'photo',
            'review',
        ]
        widgets = {
            'gig_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_photo',
            'bio',
            'location',
            'website',
        ]
