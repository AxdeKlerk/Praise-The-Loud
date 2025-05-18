## APP (gig_reviews) URLS

from django.urls import path, include
from .views import home, artist, venue, profile, review, signup, logout, delete_profile

# Add URL patterns for other views as needed
urlpatterns = [
   path('', home, name='home'), # Loads the Home page
   path('artist/', artist, name='artist'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('venue/', venue, name='venue'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('profile/', profile, name='profile'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('review/', review, name='review'), # add '<slug:slug>/' to the path if you want to pass a slug
   path('fan/', include('django.contrib.auth.urls')), # Built-in login/logout views at /fan/
   path('fan/signup/', signup, name='signup'),  # Route for user signup
   path('fan/logout/', logout, name='logout'), # Route for user logout
   path('profile/delete/', delete_profile, name='delete_profile')

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
