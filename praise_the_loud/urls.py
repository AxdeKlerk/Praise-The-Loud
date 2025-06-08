"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
## Global (praise_the_loud/urls.py)

from django.contrib import admin
from django.urls import path, include
from gig_reviews.views import home, about, artist, venue, profile, review, signup, logout, delete_profile, search_view, gallery_view
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

# Project URLs
urlpatterns = [
    path('', include('gig_reviews.urls')),  #
    path('home/', home, name='home'),  
    path('about/', about, name='about'),  
    path('profile/', profile, name='profile'),  
    path('review/', review, name='review'), 
    path('search/', search_view, name='search_view'),
    path('gallery/', gallery_view, name='gallery'),  

    # Built-in login/logout views at /fan/
    path('fan/', include('django.contrib.auth.urls')),
    
    # Your custom signup view at /fan/signup/
    path('fan/signup/', signup, name='signup'),

    # Your custom logout view at /fan/logout/
    path('fan/logout/', LogoutView.as_view(), name='logout'),
    
    # Route for deleting a profile
    path('profile/delete/', delete_profile, name='delete_profile'),
    
    # Admin site
    path('admin/', admin.site.urls),

]

# Serve static files during development
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])