from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .models import FranchiseRequest, RatingReview, ContactMessage

def home(request):
    # Get approved reviews for display
    approved_reviews = RatingReview.objects.filter(is_approved=True)[:6]
    return render(request, 'coming_soon.html', {'reviews': approved_reviews})

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def franchise(request):
    return render(request, 'franchise.html')


# ========== FORM HANDLERS ==========

@csrf_exempt
@require_http_methods(["POST"])
def submit_franchise(request):
    try:
        franchise = FranchiseRequest(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            investment_range=request.POST.get('investment_range', ''),
            remarks=request.POST.get('remarks', ''),
            consent=request.POST.get('consent') == 'on'
        )
        franchise.save()
        messages.success(request, 'Thank you for your franchise interest! Our team will contact you soon.')
    except Exception as e:
        messages.error(request, 'Something went wrong. Please try again.')
    
    return redirect('franchise')


@csrf_exempt
@require_http_methods(["POST"])
def submit_review(request):
    try:
        review = RatingReview(
            reviewer_name=request.POST.get('reviewer_name'),
            reviewer_email=request.POST.get('reviewer_email'),
            rating=int(request.POST.get('rating', 0)),
            review_message=request.POST.get('review_message'),
            consent=request.POST.get('consent') == 'on'
        )
        review.save()
        messages.success(request, 'Thank you for your review! It will appear after admin approval.')
    except Exception as e:
        messages.error(request, 'Something went wrong. Please try again.')
    
    return redirect('home')


@csrf_exempt
@require_http_methods(["POST"])
def submit_contact(request):
    try:
        contact = ContactMessage(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone', ''),
            subject=request.POST.get('subject', 'General Inquiry'),
            message=request.POST.get('message')
        )
        contact.save()
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
    except Exception as e:
        messages.error(request, 'Something went wrong. Please try again.')
    
    return redirect('contact')


# API endpoint to get reviews (for AJAX loading)
def get_reviews_api(request):
    reviews = RatingReview.objects.filter(is_approved=True).values(
        'reviewer_name', 'rating', 'review_message', 'created_at'
    )[:10]
    return JsonResponse(list(reviews), safe=False)