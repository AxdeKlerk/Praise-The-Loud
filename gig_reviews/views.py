from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import GigReviewForm
from django.utils.text import slugify
from .models import Profile



# Create your views here.
def home(request):
    return render(request, 'gig_reviews/index.html')

@login_required
def review(request):
    if request.method == 'POST':
        form = GigReviewForm(request.POST, request.FILES)
        if form.is_valid():
            gig = form.save(commit=False)
            gig.author = request.user      # set the logged-in user
            gig.slug = slugify(f"{gig.artist}-{gig.gig_date}")
            gig.save()
            return redirect('home')
    else:
        form = GigReviewForm()
    return render(request, 'gig_reviews/review.html', {'form': form})

    
def artist(request): #, slug):
    return render(request, 'gig_reviews/artist.html') #,{'slug': slug})

def venue(request): #, slug):
    return render(request, 'gig_reviews/venue.html') #,{'slug': slug})

@login_required
def profile(request): #, slug):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user, slug=slugify(request.user.username))

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'gig_reviews/profile.html', {'form': form})

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
