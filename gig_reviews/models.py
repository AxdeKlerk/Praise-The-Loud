from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class GigReview(models.Model):
    # Fields
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gig_reviews")
    # artist = models.ForeignKey("artist.Artist", on_delete=models.CASCADE, related_name="gig_reviews")
    # venue = models.ForeignKey("venue.Venue", on_delete=models.CASCADE, related_name="gig_reviews")
    gig_date = models.DateField(null=False, blank=False)
    highlight = models.CharField(max_length=100, null=False, blank=False)
    photo = models.ImageField(upload_to='gig_photos/')
    review = models.TextField(max_length=2000, null=False, blank=False)
    review_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
