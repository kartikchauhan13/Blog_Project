from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):
	cat_id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=100)
	description=models.TextField()
	image=models.ImageField(upload_to= "category/")
	url=models.CharField(max_length=200)
	add_date=models.DateTimeField(auto_now_add=True ,null=True)

	def __str__(self):
		return self.title

	def image_tag(self):
		return format_html('<img src="/media/{}" style="width:40px ; height:40px ; border-radius:50%; " >'.format(self.image))


class Post(models.Model):
	post_id=models.AutoField(primary_key=True)
	category=models.ForeignKey(Category , on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	content=HTMLField()
	image=models.ImageField(upload_to= "post/")
	url=models.CharField(max_length=200)

	def __str__(self):
		return self.title
