import pytest

from django.urls import reverse
from notes.forms import NoteForm


@pytest.mark.parametrize(
    # Define parameter names:
    'parametrized_client, note_in_list',
    (
        # Pass fixtures as parameters using "lazy fixtures":
        (pytest.lazy_fixture('author_client'), True),
        (pytest.lazy_fixture('not_author_client'), False),
    )
)
def test_notes_list_for_different_users(
        # Use the note fixture and parameters from the decorator:
        note, parametrized_client, note_in_list
):
    url = reverse('notes:list')
    # Execute the request on behalf of the parameterized client:
    response = parametrized_client.get(url)
    object_list = response.context['object_list']
    # Verify the statement "note is in the list":
    assert (note in object_list) is note_in_list


@pytest.mark.parametrize(
    # Pass name and args for reverse as parameters.
    'name, args',
    (
        # No additional arguments are needed for reverse()
        # to test the note creation page.
        ('notes:add', None),
        # Testing the note editing page requires the note's slug.
        ('notes:edit', pytest.lazy_fixture('slug_for_args'))
    )
)
def test_pages_contains_form(author_client, name, args):
    # Build the URL.
    url = reverse(name, args=args)
    # Request the specified page:
    response = author_client.get(url)
    # Check if the form object is in the context dictionary:
    assert 'form' in response.context
    # Verify the form object belongs to the correct class.
    assert isinstance(response.context['form'], NoteForm)


@pytest.fixture
def form_data():
    return {
        'title': 'New title',
        'text': 'New text',
        'slug': 'new-slug'
    }
