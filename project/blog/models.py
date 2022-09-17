from django.db import models
from django.shortcuts import reverse
class Post(models.Model):
    title = models.CharField(max_length=150,db_index=True)
    slug = models.SlugField(max_length=150,unique=True)
    body = models.TextField(db_index=True,blank=True)
    date_pub = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag',blank=True,related_name='posts')
    image = models.ImageField(upload_to='images/',default='images/defolt.png')
    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=150,db_index=True)
    slug = models.SlugField(max_length=150,unique=True)
    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})
    def __str__(self):
        return self.title

