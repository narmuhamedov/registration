from django.db import models

class Post(models.Model):
    post_name = models.CharField(max_length=100, verbose_name='Enter your post name')
    post_text = models.TextField(verbose_name='Enter your post text')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'news post'
        verbose_name_plural = 'news posts'

    def __str__(self):
        return f'{self.post_name}: {self.created_at}'
