from django.db import models

class Tag(models.Model):
    tagname = models.CharField(primary_key=True, max_length=50, default='')

    def __str__(self):
        return self.tagname


class Book(models.Model):
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    cover = models.ImageField(blank=True)
    summary = models.TextField(default='')
    quote = models.TextField(blank=True)
    pub_date = models.DateField(default='')


    tags = models.ManyToManyField(Tag)

    class Meta:
        unique_together = (('title', 'author'),)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(primary_key=True, default='')
    password = models.CharField(max_length=30, default='')
    profile_pic = models.ImageField(blank=True)
    book = models.ManyToManyField(Book,blank=True)
    def __str__(self):
        return self.username


class Feedback(models.Model):
    review = models.TextField(default='')
    rating = models.FloatField(default='')
    username = models.ManyToManyField(User)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.review









