from django.db import models

# Create your models here.
class GigReviews(models.Model):
    # Fields
    





    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    date = models.DateField()
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} by {self.artist} at {self.venue}, {self.city} on {self.date}"