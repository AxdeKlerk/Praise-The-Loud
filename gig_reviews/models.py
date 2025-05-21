from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here. 
class GigReview(models.Model):
    # Fields
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gig_reviews", null=True, blank=True)
    artist = models.ForeignKey("Artist",on_delete=models.CASCADE, related_name="gig_reviews", null=True, blank=True)
    venue = models.ForeignKey("Venue",on_delete=models.CASCADE, related_name="gig_reviews", null=True, blank=True)
    gig_date = models.DateField(null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    photo = CloudinaryField('image', default='placeholder', blank=True, null=True)
    review = models.TextField(max_length=2000, null=False, blank=False)
    review_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-gig_date']
    
    def __str__(self):
        return f"{self.artist} @ {self.venue} | {self.author} - {self.gig_date} - {self.status}"
   
class Artist(models.Model):
    # Fields
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = CloudinaryField('image', default='placeholder', blank=True, null=True)
    bio = models.TextField(max_length=2000, null=False, blank=False)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}"

class Venue(models.Model):
    # Fields
    name = models.CharField(max_length=100, null=False, blank=False)
    logo = CloudinaryField('image', default='placeholder', blank=True, null=True)
    town = models.CharField(max_length=100, null=False, blank=False)    
    post_code = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name}"
    
class Profile(models.Model):
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=2000, null=False, blank=False)
    profile_photo = CloudinaryField('image', default='placeholder', blank=True, null=True)
    location = models.CharField(max_length=100, default='UK')
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    class Meta:
        ordering = ['user']
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
