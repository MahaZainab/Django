from django.db import models
import datetime
# Create your models here.

class Rating(models.Model):
    numReviews=models.IntegerField()
    avgRating= models.FloatField()


class Book(models.Model):
    title= models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)


class Post(models.Model):
    title=  models.CharField(max_length=255)
    description=models.TextField()
    pubDate= models.DateField()
    tag=models.CharField(max_length=255)
    slug= models.SlugField(unique=True)

    def is_precovid(self):
        covid_start_date = datetime.date(2020, 3, 10)
        return self.pubDate <= covid_start_date
    
    def __str__(self):
        return self.title