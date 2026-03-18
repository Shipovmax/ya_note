from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import NoteForm
from .models import Note


class Home(generic.TemplateView):
    """Home page."""
    template_name = 'notes/home.html'


class NoteSuccess(LoginRequiredMixin, generic.TemplateView):
    """Operation success page."""
    template_name = 'notes/success.html'


class NoteBase(LoginRequiredMixin):
    """Base class for other CBVs."""
    model = Note
    success_url = reverse_lazy('notes:success')

    def get_queryset(self):
        """User can only work with their own notes."""
        return self.model.objects.filter(author=self.request.user)


class NoteCreate(NoteBase, generic.CreateView):
    """Add a note."""
    template_name = 'notes/form.html'
    form_class = NoteForm

    def form_valid(self, form):
        new_note = form.save(commit=False)
        new_note.author = self.request.user
        new_note.save()
        return super().form_valid(form)


class NoteUpdate(NoteBase, generic.UpdateView):
    """Edit a note."""
    template_name = 'notes/form.html'
    form_class = NoteForm


class NoteDelete(NoteBase, generic.DeleteView):
    """Delete a note."""
    template_name = 'notes/delete.html'


class NotesList(NoteBase, generic.ListView):
    """List of all user notes."""
    template_name = 'notes/list.html'


class NoteDetail(NoteBase, generic.DetailView):
    """Note detail view."""
    template_name = 'notes/detail.html'
