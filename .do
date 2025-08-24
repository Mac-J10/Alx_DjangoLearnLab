name: social-media-api
region: nyc1
services:
  - name: web
    github:
      repo: Mac-J10/AlxDjangoLearnLab/social-media-api
      branch: main
    build_command: |
      pip install -r requirements.txt
      python manage.py collectstatic --noinput
      python manage.py migrate --noinput
    run_command: gunicorn social_media_api.wsgi --bind 0.0.0.0:$PORT
    envs:
      - key: DJANGO_SETTINGS_MODULE
        value: social_media_api.settings
      - key: DEBUG
        value: "False"
      - key: SECRET_KEY
        from_secret: DJANGO_SECRET_KEY
      - key: DATABASE_URL
        from_secret: DATABASE_URL
    instance_size_slug: basic-xxs
    instance_count: 1