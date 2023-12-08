from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class Breed(models.Model):
    breed_name = models.CharField(max_length=500, blank=True, null=True)
    description_of_breed = models.TextField(blank=True)

    def __str__(self):
        return f"Breed: {self.breed_name}"
    
class Cattle(models.Model):
    breed_type = models.ForeignKey(Breed, on_delete=models.CASCADE, blank=True)
    Age = models.IntegerField(blank=True)
    image = models.ImageField(upload_to="cattles/")
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    stock = models.BooleanField(default=False)

    class Meta:
        ordering = ['-Age']

    def __str__(self):
        return f"Cattle: {self.name}; Breed Type: {self.breed_type.breed_name}"
    
class Sheep(models.Model):
    breed_type = models.ForeignKey(Breed, on_delete=models.CASCADE, blank=True)
    Age = models.IntegerField(blank=True)
    image = models.ImageField(upload_to="sheep/")
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    stock = models.BooleanField(default=False)

    class Meta:
        ordering = ['-Age']

    def __str__(self):
        return f"Sheep: {self.name}; Breed Type: {self.breed_type.breed_name}"
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    tel = models.CharField(max_length=13, blank=True, null=True, verbose_name="Telephone Number")

    def __str__(self):
        return f"Contact Message From: {self.first_name} {self.last_name}"
    
# Blog Model 
class Post(models.Model):
    title = models.CharField(max_length=255)
    hearder_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    post_time = models.DateTimeField(auto_now_add=True)
    Category =  models.CharField( max_length=50)
    Snippet =  models.CharField( max_length=50)
    
    
    def __str__(self):
        return self.title + ' | ' 

    def get_absolute_url(self):
        return reverse("website:article-detail", kwargs={"pk": self.pk})
    
# Career Model/ 
class JobPost(models.Model):
    """
    Job Opening model fields may be
    adjusted for optional modeling
    """
    title = models.CharField(max_length=300, blank=True, null=True)
    closing_date = models.DateField(editable=True, blank=True)
    number_of_open_position = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
    
class FarmOperation(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    details = models.TextField(blank=True)
    image1 = models.ImageField(upload_to="operations/", blank=True)
    image2 = models.ImageField(upload_to="operations/", blank=True)

    def __str__(self):
        return self.name
    
class JobApplicant(models.Model):
    fullname = models.CharField(max_length=800, blank=True, null=True)
    phonenumber = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(blank=True)
    resume = models.FileField(blank=True, upload_to="resumes/")
    motivational_letter = models.TextField(blank=True)

    def __str__(self):
        return self.fullname