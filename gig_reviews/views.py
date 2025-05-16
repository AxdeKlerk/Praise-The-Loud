from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def submit_review(request):
    return render(request, 'gig_reviews/submit_review.html')
    
