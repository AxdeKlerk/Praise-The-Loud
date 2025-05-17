## APP (gig_reviews) URLS

from django.urls import path
from . import views

# Add URL patterns for other views as needed
urlpatterns = [
   path('', views.home, name='home'), # Loads the Home page
   path('home/', views.home, name='home'),# Displays the homepage with an overview of recent reviews or featured content
   path('artist/', views.artist, name='artist'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('venue/', views.venue, name='venue'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('profile/', views.user_profile, name='profile'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('review/', views.review, name='review'), # add '<slug:slug>/' to the path if you want to pass a slug
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
