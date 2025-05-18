from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import GigReviewForm
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.contrib import messages


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
def profile(request):
    try:
        profile = request.user.profile
        profile_exists = True
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile_exists = False

    editing = request.GET.get('edit') == 'true' or not profile_exists

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')  # redirect to view mode
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'profile_exists': profile_exists,
        'editing': editing,
    }
    return render(request, 'gig_reviews/profile.html', context)

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

@login_required
def delete_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, "Your profile has been deleted.")
        return redirect('profile')
