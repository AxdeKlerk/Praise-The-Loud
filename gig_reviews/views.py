from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'gig_reviews/index.html')
                  
def review(request):
    return render(request, 'gig_reviews/review.html')
#     # Fetch review details from the database using the slug
    
def artist(request): #, slug):
    return render(request, 'gig_reviews/artist.html') #,{'slug': slug})

def venue(request): #, slug):
    return render(request, 'gig_reviews/venue.html') #,{'slug': slug})

def profile(request): #, slug):
    return render(request, 'gig_reviews/profile.html') #,{'slug': slug})

# def artist(request, slug):
#     # Fetch artist details from the database using the slug