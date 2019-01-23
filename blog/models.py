from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User
from django.utils.html import format_html
import  datetime


# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def colored_status(self):
        if self.author.username == 'admin':
            colored = 'red'
        else:
            colored ='green'
        return format_html(
            '<span style="color: {};">{}</span>',
            colored,
            self.author,
        )
    colored_status.short_description=u'作者'