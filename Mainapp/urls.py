from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('franchise/', views.franchise, name='franchise'),
    
    # Form submission URLs
    path('submit-franchise/', views.submit_franchise, name='submit_franchise'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),
    path('api/reviews/', views.get_reviews_api, name='get_reviews_api'),
]