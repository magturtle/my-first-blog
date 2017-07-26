from django.db import models
from django.utils import timezone


class Post(models.Model):#parent class
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)#all attirbutes

    def publish(self):
        self.published_date = timezone.now()
        self.save() #self means the class and the parent class

    def __str__(self):
        return self.title
