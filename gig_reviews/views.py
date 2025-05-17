from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


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

@login_required
def profile(request): #, slug):
    return render(request, 'gig_reviews/profile.html') #,{'slug': slug})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)           # log them in immediately
            return redirect('home')        # send them to home page
    else:
        form = UserCreationForm()
    return render(request, 'gig_reviews/signup.html', {'form': form})

def logout(request):
    return render(request, 'gig_reviews/logout.html')
