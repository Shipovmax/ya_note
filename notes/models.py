from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Note(models.Model):
    title = models.CharField(
        'Title',
        max_length=100,
        default='Note title',
        help_text='Give a short title to the note'
    )
    text = models.TextField(
        'Text',
        help_text='Add details'
    )
    slug = models.SlugField(
        'Slug for the note page',
        max_length=100,
        unique=True,
        blank=True,
        help_text=('Provide a slug for the note page. Use only '
                   'Latin letters, numbers, hyphens and underscores')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            max_slug_length = self._meta.get_field('slug').max_length
            self.slug = slugify(self.title)[:max_slug_length]
        super().save(*args, **kwargs)
