from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    blog_image = models.ImageField(upload_to='blogimage', blank=True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if self.userID and self.userID.is_superuser:
            super().save(*args, **kwargs)

        else:
            print('Cannot create BlogPost')



    def __str__(self):
        return self.title
    
