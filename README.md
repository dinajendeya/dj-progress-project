# Dina Jendeya — Learning Journey Website

A small Django site to share progress from my cybersecurity mentorship journey: Linux, CCNA networking, Python, OverTheWire Bandit, TryHackMe Security 101, and building this blog.

## Stack

- Django 5
- SQLite (local) — swap to PostgreSQL via `DATABASES` for production
- Plain templates + a custom CSS theme (cyber/tech, dark)

## Project layout

```
config/                 Django project (settings, urls, wsgi)
apps/
  core/                 Site profile, home/about/contact
  progress/             Topics, progress entries, milestones
  blog/                 Long-form posts
templates/              Shared base + per-app templates
static/css/site.css     Theme
```

## Local setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py seed_demo          # optional: load topics + sample content
python manage.py createsuperuser
python manage.py runserver
```

Visit:

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Content workflow

1. Open the Django admin.
2. Edit **Site profile** (singleton) for name, tagline, bio, mentorship blurb, and contact links.
3. Add **Topics** (Linux, CCNA, Python, Bandit, TryHackMe, Building this blog).
4. Add **Progress entries** to a topic and set status to _Published_ to make them visible.
5. Add **Milestones** for visible wins.
6. Use the **Blog** section for longer-form posts; mark _Featured_ to surface on the homepage.

Drafts are not visible on the public site.

## Pages

- `/` — Home (intro, tracks, latest entries + milestones, featured posts)
- `/about/` — About Dina
- `/journey/` — All learning tracks
- `/journey/<slug>/` — Topic detail (entries + milestones)
- `/journey/milestones/` — All milestones
- `/blog/` and `/blog/<slug>/` — Posts
- `/contact/` — Contact links
- `/admin/` — Django admin

## Deployment notes

- Set `DJANGO_DEBUG=False` and provide a strong `DJANGO_SECRET_KEY`.
- Set `DJANGO_ALLOWED_HOSTS` (e.g. `dina.example.com`) and `DJANGO_CSRF_TRUSTED_ORIGINS` (e.g. `https://dina.example.com`).
- Run `python manage.py collectstatic` and serve `staticfiles/` (e.g. via WhiteNoise or your platform's static hosting).
- For PostgreSQL, install `psycopg[binary]` and update `DATABASES` in `config/settings.py` to read from a `DATABASE_URL` env var.
- Production-ready WSGI entry: `gunicorn config.wsgi:application` (Linux hosts).

Suggested hosts: Render, Railway, Fly.io, or Azure App Service.
