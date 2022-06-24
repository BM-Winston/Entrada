from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', null=True)
    bio = models.TextField()
    email=models.EmailField(null=True)
    
    


    def __str__(self):
        return self.user.username


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()


class Post(models.Model):
    image=models.ImageField(upload_to='images/',null=True)
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=500)
    url= models.URLField(max_length=200)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):

        self.update()

    @classmethod
    def get_post(cls,searchTerm):
        titles=cls.objects.filter(title__icontains=searchTerm)
        return titles