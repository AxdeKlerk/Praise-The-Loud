from django.contrib import admin
from .models import GigReview, Artist, Venue, Profile

# Register your models here.
admin.site.register(GigReview)
admin.site.register(Artist)
admin.site.register(Venue)
admin.site.register(Profile)
