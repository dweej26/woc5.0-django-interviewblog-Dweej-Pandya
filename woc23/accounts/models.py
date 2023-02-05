from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here
class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    title=models.CharField(max_length=255)
    status=models.CharField(max_length=255,default='draft')
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    favourites=models.ManyToManyField(User,related_name='favourites',default=None,blank=True)
    objects=models.Manager() 
    newmanager=NewManager()
    def __str__(self):
        return '"' +self.title + '" by ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("postslist", args=(str(self.id)))
    
    
    
class Company_Name(models.Model):
    id= models.AutoField
    name = models.CharField(max_length=200, null=True)
    Offer_Type= models.CharField(max_length=200, null=True)
    Job_Profile=models.CharField(max_length=200, null=True)
    year= models.CharField(max_length=4)
    content=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

    