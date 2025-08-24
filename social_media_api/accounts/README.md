## Follow System

- `POST /api/accounts/follow/<user_id>/` — Follow a user
- `POST /api/accounts/unfollow/<user_id>/` — Unfollow a user

## Feed

- `GET /api/feed/` — Returns posts from followed users, ordered by newest first

### Example

```http
POST /api/accounts/follow/3/
Authorization: Token <your_token>
```

```json
{
    "message": "You are now following user 3."
}


---

Deliverables Summary

| Category                     | Files / Artifacts                                                                 |
|-----------------------------|------------------------------------------------------------------------------------|
| 🔧 Updated Models           | `accounts/models.py` with `following` and `followers` fields                      |
| 🧠 Views                    | `accounts/views.py` (follow/unfollow), `posts/views.py` (feed)                    |
| 🔗 URL Configs              | `accounts/urls.py`, `posts/urls.py`                                               |
| 📄 Docs                     | README updates with endpoint usage and examples                                   |
| 🧪 Testing                  | Postman collection or curl scripts validating follow logic and feed accuracy      |

