import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class PublishedManager(models.Manager):
     def get_queryset(self):
          return super(PublishedManager, self).get_queryset().filter(status='published')

class Book(models.Model):

     STATUS_CHOICES = (
                        ('draft', 'Draft'),
                        ('published', 'Published'),
    )

     id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
     slug = models.SlugField(max_length=250, unique_for_date='publish')
     publish = models.DateTimeField(default=timezone.now)
     title = models.CharField(max_length=100)
     author = models.CharField(max_length=100)
     price = models.DecimalField(max_digits=7, decimal_places=2)
     old_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
     cover = models.ImageField(upload_to='covers/', blank=True)

     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
     body = RichTextUploadingField(blank=True, null=True, config_name='special')

     published = PublishedManager()

     def __str__(self):
          return self.title

     def get_absolute_url(self): 
          return reverse('book:book_detail', args=[str(self.id)])

     # def get_absolute_url(self):
     #    return reverse('post:post_detail',
     #                                    args=[self.publish.year,
     #                                    self.publish.month,
     #                                    self.publish.day, self.slug])