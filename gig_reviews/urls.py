## APP (gig_reviews) URLS

from django.urls import path
from . import views

# Add URL patterns for other views as needed
urlpatterns = [
   path('', views.submit_review, name='submit_review'),
   path('artist/<slug:slug>/', views.artist, name='artist'),
   path('venue/<slug:slug>/', views.venue, name='venue'),
   path('profile/<slug:slug>/', views.user_profile, name='user_profile'),
   # path('review/<slug:slug>/', views.review, name='review'), 
]