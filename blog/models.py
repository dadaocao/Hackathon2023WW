from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Publish'))


# Create your models here.

# add
class Post(models.Model):  # all the fields below
    title = models.CharField(max_length=200)   # 1
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()    # 2
    date_created = models.DateTimeField(auto_now_add=True)  # 3 generate the time
    slug = models.SlugField(max_length=200, unique=True)  # 4 make sure there won't be the same url
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)  # 5 # CASCADE delete also the user posts
    status = models.IntegerField(choices=STATUS, default=0)  # 6 save draft

    def __str__(self):
        return self.title
