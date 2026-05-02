from django.contrib import admin
from .models import FranchiseRequest, RatingReview, ContactMessage

@admin.register(FranchiseRequest)
class FranchiseRequestAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'city', 'state', 'phone', 'investment_range', 'created_at', 'is_contacted']
    list_filter = ['is_contacted', 'investment_range', 'city', 'created_at']
    search_fields = ['full_name', 'email', 'phone', 'city', 'state']
    readonly_fields = ['created_at']
    list_editable = ['is_contacted']
    list_per_page = 20
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('Location Details', {
            'fields': ('city', 'state')
        }),
        ('Franchise Details', {
            'fields': ('investment_range', 'remarks')
        }),
        ('Status', {
            'fields': ('consent', 'is_contacted', 'created_at')
        }),
    )


@admin.register(RatingReview)
class RatingReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewer_name', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['reviewer_name', 'reviewer_email', 'review_message']
    readonly_fields = ['created_at']
    list_editable = ['is_approved']
    list_per_page = 20
    fieldsets = (
        ('Reviewer Details', {
            'fields': ('reviewer_name', 'reviewer_email')
        }),
        ('Review Details', {
            'fields': ('rating', 'review_message')
        }),
        ('Status', {
            'fields': ('consent', 'is_approved', 'created_at')
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'created_at', 'is_replied']
    list_filter = ['subject', 'is_replied', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_replied']
    list_per_page = 20
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_replied', 'created_at')
        }),
    )