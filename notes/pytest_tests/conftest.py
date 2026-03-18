import pytest

# Import the client class.
from django.test.client import Client

# Import the note model to create an instance.
from notes.models import Note


@pytest.fixture
# Use the built-in fixture for the django_user_model.
def author(django_user_model):
    return django_user_model.objects.create(username='Author')


@pytest.fixture
def not_author(django_user_model):
    return django_user_model.objects.create(username='Not Author')


@pytest.fixture
def author_client(author):  # Call the author fixture.
    # Create a new client instance to avoid changing the global one.
    client = Client()
    client.force_login(author)  # Log in the author to the client.
    return client


@pytest.fixture
def not_author_client(not_author):
    client = Client()
    client.force_login(not_author)  # Log in a regular user to the client.
    return client


@pytest.fixture
def note(author):
    note = Note.objects.create(  # Create a note object.
        title='Title',
        text='Note text',
        slug='note-slug',
        author=author,
    )
    return note


@pytest.fixture
# Fixture requests another note creation fixture.
def slug_for_args(note):
    # And returns a tuple containing the note slug.
    # The comma at the end indicates that it is a tuple.
    return (note.slug,)
