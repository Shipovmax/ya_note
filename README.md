# YaNote

YaNote is a simple Django-based web application for managing personal notes. It allows users to create, view, edit, and delete their notes with ease.

## Features

- **Note Management**: Create, view, update, and delete notes.
- **User Authentication**: Secure sign-up, login, and logout functionality.
- **Access Control**: Users can only see and manage their own notes.
- **Slug Generation**: Automatic URL-friendly slug generation for note titles.

## Tech Stack

- **Framework**: [Django 3.x](https://www.djangoproject.com/)
- **Database**: SQLite3
- **Testing**: [Pytest-Django](https://pytest-django.readthedocs.io/en/latest/)
- **CSS**: Bootstrap

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd ya_note
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Running Tests

To run the project's tests, use `pytest`:
```bash
pytest
```

## License

This project is for educational purposes.
