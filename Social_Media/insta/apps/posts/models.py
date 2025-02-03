from django.db import models

# Create your models here.
class UserPost(models.Model):
    id=models.AutoField(primary_key=True)
    caption=models.CharField(max_length=500)
    post_img=models.ImageField(null=True,blank=True,upload_to="post_img/")
    date=models.DateField(auto_now_add=True)