from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField



class Profile(models.Model):
	username = models.CharField(default='User',max_length=30)
	profile_pic = CloudinaryField()
	bio = models.TextField(default='',blank = True)
	first_name = models.CharField(max_length =30)
	last_name = models.CharField(max_length =30)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

	@classmethod
	def search_profile(cls,search_term):
		got_profiles = cls.objects.filter(first_name__icontains = search_term)
		return got_profiles

class Tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = CloudinaryField()

    def __str__(self):
        return self.title
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls, search_tearm):
        news = cls.objects.filter(title__icontains=search_tearm)

        return news
