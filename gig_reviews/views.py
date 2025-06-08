from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import GigReviewForm, ProfileForm, FanContactForm, ArtistContactForm, VenueContactForm, SearchForm #, CustomUserCreationForm
from .models import Profile, Artist, Venue, GigReview
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.
def home(request):
    form = SearchForm()
    return render(request, 'gig_reviews/index.html', {'form': form})

def about(request):
    form = SearchForm()
    return render(request, 'gig_reviews/about.html', {'form': form})

@login_required
def review(request):
    if request.method == 'POST':
        form = GigReviewForm(request.POST, request.FILES)
        if form.is_valid():
            gig = form.save(commit=False)
            gig.author = request.user      
            gig.slug = slugify(f"{gig.artist}-{gig.gig_date}")
            gig.save()
            return redirect('profile')  # redirect to profile page after saving review
    else:
        form = GigReviewForm()
    return render(request, 'gig_reviews/new_review.html', {'form': form})

    
def artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    reviews = GigReview.objects.filter(artist=artist)
    return render(request, 'gig_reviews/artist.html', {'artist': artist})

def venue(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    reviews = GigReview.objects.filter(venue=venue)
    return render(request, 'gig_reviews/venue.html', {'venue': venue})

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

    reviews = GigReview.objects.filter(author=request.user).order_by('-review_date')

    context = {
        'form': form,
        'profile': profile,
        'profile_exists': profile_exists,
        'editing': editing,
        'reviews': reviews
    }
    return render(request, 'gig_reviews/profile.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
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


def contact_view(request):
    fan_form = FanContactForm()
    artist_form = ArtistContactForm()
    venue_form = VenueContactForm()

    if request.method == "POST":
        user_type = request.POST.get("user_type")

        if user_type == "fan":
            fan_form = FanContactForm(request.POST)
            if fan_form.is_valid():
                return redirect("thank_you")

        elif user_type == "artist":
            artist_form = ArtistContactForm(request.POST, request.FILES)
            if artist_form.is_valid():
                return redirect("thank_you")

        elif user_type == "venue":
            venue_form = VenueContactForm(request.POST, request.FILES)
            if venue_form.is_valid():
                return redirect("thank_you")

    return render(request, "gig_reviews/contact_modal.html", {
        "fan_form": fan_form,
        "artist_form": artist_form,
        "venue_form": venue_form
    })


def thank_you(request):
    return render(request, "gig_reviews/thank_you.html")


def search_view(request):
    if request.method == 'GET':
        form = SearchForm(request.GET or None)
        results = []
        reviews = []

        if form.is_valid():
            search_type = form.cleaned_data['search_type']
            query = form.cleaned_data['search_term']

            if search_type == 'artist':
                results = Artist.objects.filter(name__icontains=query)
                reviews = GigReview.objects.filter(artist__in=results)
                
                for item in results:
                    item.reviews = GigReview.objects.filter(artist=item) 

            elif search_type == 'venue':
                results = Venue.objects.filter(name__icontains=query)
                reviews = GigReview.objects.filter(venue__in=results)
                
                for item in results:
                    item.reviews = GigReview.objects.filter(venue=item)

        return render(request, 'gig_reviews/search_results.html', {
            'form': form,
            'results': results,
            'reviews': reviews,
        })


def gallery_view(request):
    reviews_with_photos = GigReview.objects.filter(photo__isnull=False).order_by('-gig_date')
    return render(request, 'gig_reviews/gallery.html', {
        'reviews': reviews_with_photos
    })


def author_profile(request, pk):
    author = get_object_or_404(User, pk=pk)
    
    try:
        profile = author.profile  # this assumes you have a OneToOneField in your Profile model
    except Profile.DoesNotExist:
        profile = None

    reviews = GigReview.objects.filter(author=author).order_by('-review_date')

    return render(request, 'gig_reviews/author_profile.html', {
        'author': author,
        'profile': profile,
        'reviews': reviews,
    })