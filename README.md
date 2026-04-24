# YaNote

A Django note-taking app with full CRUD, auto-slug generation, and a pytest test suite covering routes and content isolation.

---

## Features

- **Note CRUD** — create, read, update, delete via Django CBVs
- **Auth-gated** — all note operations require login (`LoginRequiredMixin`); unauthenticated requests redirect to login
- **Author isolation** — `get_queryset` filters by `request.user`; users only see and modify their own notes
- **Auto-slug** — `Note.save()` auto-generates slug from title via `slugify` if left blank; unique constraint enforced
- **Slug validation** — `NoteForm.clean_slug()` raises `ValidationError` on duplicate slugs
- **Registration** — built-in Django auth views for sign up / login / logout

---

## Tech Stack

| | |
|---|---|
| Language | Python 3 |
| Framework | Django 3.2 |
| Testing | pytest, pytest-django, pytest-lazy-fixture, pytest-subtests |
| Linting | flake8, flake8-docstrings, pep8-naming |

---

## Quick Start

```bash
git clone https://github.com/Shipovmax/ya_note
cd ya_note

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Running Tests

```bash
pytest
```

| Test file | Coverage |
|-----------|---------|
| `test_routes.py` | Redirect behaviour for anonymous users on all protected URLs |
| `test_content.py` | Note list isolation per user; form presence on add/edit pages |

---

## Project Structure

```
ya_note/
├── notes/
│   ├── models.py       # Note model with auto-slug
│   ├── views.py        # CBVs: Home, List, Detail, Create, Update, Delete
│   ├── forms.py        # NoteForm with slug validation
│   ├── urls.py
│   └── pytest_tests/
│       ├── conftest.py
│       ├── test_routes.py
│       └── test_content.py
├── templates/
│   ├── notes/
│   └── registration/
└── yanote/             # Django settings and root URLs
```

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
