import os

import dj_database_url

from .base import *  # noqa: F403

DEBUG = False

if not SECRET_KEY or SECRET_KEY == "unsafe-development-key-change-me":
    raise RuntimeError("Set a secure SECRET_KEY environment variable for production.")

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("Set DATABASE_URL to a PostgreSQL connection URL for production.")

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=os.environ.get("DATABASE_SSL_REQUIRE", "false").lower() == "true",
    )
}
CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if origin.strip()]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = os.environ.get("SECURE_COOKIES", "true").lower() == "true"
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE
