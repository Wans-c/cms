# Wagtail CMS

A minimal Wagtail project with a Docker-based deployment scaffold.

## Run locally

1. Copy `.env.example` to `.env` and set a long, random `SECRET_KEY` and a unique `POSTGRES_PASSWORD`.
2. Start the app and PostgreSQL:

   ```bash
   docker compose up --build
   ```

3. Create an administrator account:

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

4. Open <http://localhost:8000/admin/>.

## Deploy

Build and run the included Dockerfile on a host that supports Docker. Configure these environment variables on the host:

- `DJANGO_SETTINGS_MODULE=cms.settings.production`
- `SECRET_KEY` — a secure, unique secret
- `DATABASE_URL` — PostgreSQL connection URL
- `ALLOWED_HOSTS` — comma-separated hostnames
- `CSRF_TRUSTED_ORIGINS` — comma-separated full origins, e.g. `https://cms.example.com`

The container runs database migrations and collects static assets on startup. Configure persistent media storage (or external object storage) before accepting uploads. Use a managed PostgreSQL database for production.

This adds the Wagtail application and deployment configuration to the repository; it does not make the site publicly accessible by itself. A hosting provider, database, secrets, and domain still need to be configured.
