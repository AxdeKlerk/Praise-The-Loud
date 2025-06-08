## APP (gig_reviews) URLS

from django.urls import path, include
from .views import home, about, artist, venue, profile, review, signup, logout, delete_profile, contact_view, thank_you, search_view, gallery_view, author_profile

# Add URL patterns for other views as needed
urlpatterns = [
   path('', home, name='home'), 
   path('about/', about, name='about'), 
   path('artist/<int:pk>/', artist, name='artist_profile'), 
   path('venue/<int:pk>/', venue, name='venue_profile'), 
   path('author/<int:pk>/', author_profile, name='author_profile'),
   path('profile/', profile, name='profile'), 
   path('new-review/', review, name='new_review'),
   path('fan/', include('django.contrib.auth.urls')), 
   path('fan/signup/', signup, name='signup'), 
   path('fan/logout/', logout, name='logout'),
   path('profile/delete/', delete_profile, name='delete_profile'), 
   path('contact/', contact_view, name='contact'), 
   path('thank-you/', thank_you, name='thank_you'), 
   path('search/', search_view, name='search_view'), 
   path('gallery/', gallery_view, name='gallery'), 

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
