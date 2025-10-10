from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=60)
    content = models.TextField()
    published_date = models.DateField(auto_now=True)
    post_image= models.ImageField(upload_to='post', default='post/1.png')

    def __str__(self):
        return self.post_title
    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)