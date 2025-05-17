from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class GigReview(models.Model):
    # Fields
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gig_reviews")
    artist = models.ForeignKey("Artist",on_delete=models.CASCADE, related_name="gig_reviews")
    venue = models.ForeignKey("Venue",on_delete=models.CASCADE, related_name="gig_reviews")
    gig_date = models.DateField(null=False, blank=False)
    highlight = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ImageField(upload_to='gig_photos/')
    review = models.TextField(max_length=2000, null=False, blank=False)
    review_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-gig_date']
    
    def __str__(self):
        return f"{self.venue} - {self.gig_date} - {self.status} - {self.slug}"
    # add "{self.artist} @ {self.venue} | {self.author} to the return string once user model is set up
   
class Artist(models.Model):
    # Fields
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.ImageField(upload_to='artist_photos/')
    bio = models.TextField(max_length=2000, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}- {self.logo}- {self.bio} - {self.slug}"

class Venue(models.Model):
    # Fields
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = models.ImageField(upload_to='venue_photos/')
    town = models.CharField(max_length=100, null=False, blank=False)    
    post_code = models.CharField(max_length=20, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}- {self.logo}- {self.town} - {self.post_code} - {self.slug}"
    
class Profile(models.Model):
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=2000, null=False, blank=False)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['user']
    
    def __str__(self):
        return f"{self.user} - {self.profile_photo} {self.bio} - {self.slug}"
