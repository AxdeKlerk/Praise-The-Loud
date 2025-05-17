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
from django.urls import path
from gig_reviews.views import home, review, artist, venue, profile  # import directly from the app


urlpatterns = [
    path('', home, name='home'),  # Loads the Home page
    path('home/', home, name='home'),  # Route back to the Home page
    path('review/', review, name='review'), # Route for submitting a gig review
    path('artist/', artist, name='artist'),  # Route for artist details
    path('venue/', venue, name='venue'),  # Route for venue details
    path('profile/', profile, name='profile'),  # Route for user profile
    path('admin/', admin.site.urls),
]