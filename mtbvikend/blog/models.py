from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=20)
    text = models.TextField()
    #photo = models.FileField(default='', upload_to='uploads/%Y/%m/%d/')
    photo = models.ImageField()
    #photo_path = post.photo.url
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #def get_absolute_url(self):
    #    return reverse('music:detail', kwargs={'pk': self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
