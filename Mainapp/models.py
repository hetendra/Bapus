from django.db import models
from django.utils import timezone

class FranchiseRequest(models.Model):
    INVESTMENT_CHOICES = [
        ('10-25 Lakhs', '10-25 Lakhs'),
        ('25-50 Lakhs', '25-50 Lakhs'),
        ('50 Lakhs - 1 Crore', '50 Lakhs - 1 Crore'),
        ('1 Crore+', '1 Crore+'),
    ]
    
    full_name = models.CharField(max_length=200, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=100, verbose_name="State")
    investment_range = models.CharField(max_length=50, choices=INVESTMENT_CHOICES, blank=True, null=True, verbose_name="Expected Investment Range")
    remarks = models.TextField(blank=True, null=True, verbose_name="Additional Remarks")
    consent = models.BooleanField(default=True, verbose_name="Consent Given")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Submitted On")
    is_contacted = models.BooleanField(default=False, verbose_name="Contacted")
    
    class Meta:
        verbose_name = "Franchise Request"
        verbose_name_plural = "Franchise Requests"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.city} ({self.created_at.strftime('%d/%m/%Y')})"


class RatingReview(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    reviewer_name = models.CharField(max_length=200, verbose_name="Reviewer Name")
    reviewer_email = models.EmailField(verbose_name="Email Address")
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Rating")
    review_message = models.TextField(verbose_name="Review Message")
    consent = models.BooleanField(default=True, verbose_name="Consent Given")
    is_approved = models.BooleanField(default=False, verbose_name="Approved for Display")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Submitted On")
    
    class Meta:
        verbose_name = "Rating & Review"
        verbose_name_plural = "Ratings & Reviews"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.reviewer_name} - {self.rating} Stars ({self.created_at.strftime('%d/%m/%Y')})"


class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('General Inquiry', 'General Inquiry'),
        ('Franchise Request', 'Franchise Request'),
        ('Investment Interest', 'Investment Interest'),
        ('Feedback', 'Feedback'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone Number")
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='General Inquiry', verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    is_replied = models.BooleanField(default=False, verbose_name="Replied")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Submitted On")
    
    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%d/%m/%Y')})"