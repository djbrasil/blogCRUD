from django.db import models
from django.utils import timezone 
from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    title = models.CharField('Titulo',max_length=200)
    text = models.TextField('Descrição')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

