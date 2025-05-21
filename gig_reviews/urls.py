## APP (gig_reviews) URLS

from django.urls import path, include
from .views import home, about, artist, venue, profile, review, signup, logout, delete_profile, contact_view, thank_you, search_view

# Add URL patterns for other views as needed
urlpatterns = [
   path('', home, name='home'), # Loads the Home page
   path('about/', about, name='about'),  # Route to the About page
   path('artist/', artist, name='artist'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('venue/', venue, name='venue'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('profile/', profile, name='profile'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('new-review/', review, name='new_review'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('fan/', include('django.contrib.auth.urls')), # Built-in login/logout views at /fan/
   path('fan/signup/', signup, name='signup'),  # Route for user signup
   path('fan/logout/', logout, name='logout'), # Route for user logout
   path('profile/delete/', delete_profile, name='delete_profile'), # Route for deleting user profile
   path('contact/', contact_view, name='contact'), # Route for contact form
   path("thank-you/", thank_you, name="thank_you"), # Route for thank you page
   path('search/', search_view, name='search'), # Route for search view

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
