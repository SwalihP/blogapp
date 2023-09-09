from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title=models.CharField(max_length=200,unique=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='img',null=True,blank=True)
    author=models.CharField(max_length=20)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
