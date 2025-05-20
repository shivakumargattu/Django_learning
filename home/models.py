from django.db import models

class Home(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Home Title",
        help_text="Enter the title for this home listing"
    )
    
    image = models.ImageField(
        upload_to='home_images/',
        verbose_name="Home Image",
        help_text="Upload an image of the home",
        blank=True,  # Makes the field optional
        null=True    # Allows NULL in database
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home Listing"
        verbose_name_plural = "Home Listings"
        ordering = ['-created_at']