from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User



class Blog(models.Model):
    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
        ('Pending', 'Pending')
    )
    title = models.CharField(max_length= 100, blank= False )
    description = models.CharField(max_length= 160 , blank= False)
    content = RichTextField()
    slug = models.SlugField(max_length= 100, unique= True, blank= False)
    status = models.CharField(max_length= 15, choices= STATUS, blank= False)
    Date = models.DateField(auto_now= True)

    def __str__(self):
        return self.title


