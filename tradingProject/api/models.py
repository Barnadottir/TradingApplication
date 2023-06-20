from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

#class Post(models.Model):
#    user_name = models.CharField(max_length=20,unique=True)
#    user_password = models.CharField(max_length=50)