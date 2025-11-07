# ABOD Website

A Django-based website for ABOD architecture and design firm.

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Collect static files: `python manage.py collectstatic`
7. Run the development server: `python manage.py runserver`

## Deployment on Render

This application is configured for deployment on Render.com.

### Environment Variables

Set the following environment variables in your Render dashboard:

- `DEBUG`: Set to `False` for production
- `SECRET_KEY`: A secure random string for Django
- `ALLOWED_HOSTS`: Your Render domain (e.g., `your-app.onrender.com`)
- `DATABASE_URL`: PostgreSQL database URL (optional, defaults to SQLite)
- `SECURE_SSL_REDIRECT`: Set to `True` for HTTPS redirect
- `SESSION_COOKIE_SECURE`: Set to `True` for secure cookies
- `CSRF_COOKIE_SECURE`: Set to `True` for secure CSRF cookies

### Deployment Steps

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set the build command: `pip install -r requirements.txt`
4. Set the start command: `python manage.py migrate && python manage.py collectstatic --noinput && gunicorn ABOD.wsgi:application --bind 0.0.0.0:$PORT`
5. Add the environment variables listed above
6. Deploy!

## Features

- Multi-language support (English, French, German)
- Responsive design
- Project showcase
- Service pages
- News section
- Contact forms