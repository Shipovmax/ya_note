from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from .models import Note

WARNING = ' - this slug already exists, choose a unique value!'


class NoteForm(forms.ModelForm):
    """Form for creating or updating a note."""

    class Meta:
        model = Note
        fields = ('title', 'text', 'slug')

    def clean_slug(self):
        """Handle case where slug is not unique."""
        cleaned_data = super().clean()
        slug = cleaned_data.get('slug')
        if not slug:
            title = cleaned_data.get('title')
            slug = slugify(title)[:100]
        if Note.objects.filter(
                slug=slug
        ).exclude(id=self.instance.pk).exists():
            raise ValidationError(slug + WARNING)
        return slug
