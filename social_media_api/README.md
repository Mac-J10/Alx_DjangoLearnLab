# social_media_api

A Django REST Framework API for user authentication with token-based access.

## Setup

1. Clone the repo  
2. Create a virtual environment and install dependencies  
   ```bash
   pip install -r requirements.txt


## Likes

- POST `/api/posts/{post_id}/like/` — Like a post  
- POST `/api/posts/{post_id}/unlike/` — Unlike a post  

Example request:

```http
POST /api/posts/1/like/
Authorization: Token your_token
```

```http
POST /api/posts/1/unlike/
Authorization: Token your_token


---

## Deliverables Summary

| Category                  | Files / Artifacts                                                     |
|---------------------------|------------------------------------------------------------------------|
| Models                    | `posts/models.py` (Like), `notifications/models.py` (Notification)  |
| Serializers               | `posts/serializers.py`, `notifications/serializers.py`               |
| Views                     | `posts/views.py`, `notifications/views.py`                           |
| URL Configurations        | `posts/urls.py`, `notifications/urls.py`, root `urls.py` includes   |
| Tests                     | `tests/test_likes.py`, `tests/test_notifications.py`                 |
| Documentation             | README snippet with endpoints and examples                             |
