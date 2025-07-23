# Tell Django to use our custom user model
AUTH_USER_MODEL = "accounts.CustomUser"

# Optional: configure media uploads
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"