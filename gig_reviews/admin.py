from django.contrib import admin
from .models import GigReview, Artist, Venue, Profile

# Register your models here.
admin.site.register(GigReview)

#Add search functionality to the admin panel
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
