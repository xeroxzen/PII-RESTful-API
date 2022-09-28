import uuid
from django.db import models

class Pii(models.Model):
    # Create a model for the PII data
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    ip = models.GenericIPAddressField()
    cc = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    ssn = models.CharField(max_length=100)
    dob = models.DateField()
    hobbies = models.CharField(max_length=100)
    interests = models.CharField(max_length=100)
    favorite_color = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)
    geocoordinates = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    relationships = models.CharField(max_length=100)
    pets = models.CharField(max_length=100) 
    facebook_handle = models.CharField(max_length=100)
    twitter_handle = models.CharField(max_length=100)
    instagram_handle = models.CharField(max_length=100)
    snapchat_handle = models.CharField(max_length=100)
    tiktok_handle = models.CharField(max_length=100)
    youtube_handle = models.CharField(max_length=100)
    linkedin_handle = models.CharField(max_length=100)
    pinterest_handle = models.CharField(max_length=100)
    reddit_handle = models.CharField(max_length=100)
    twitch_handle = models.CharField(max_length=100)
    github_handle = models.CharField(max_length=100)
    bitcoin_hash = models.CharField(max_length=100)
    ethereum_hash = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']

    
