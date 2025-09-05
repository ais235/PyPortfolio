# day10/api_basics.py
from __future__ import annotations
from typing import Any, Dict, Optional
import json
from pathlib import Path

import requests
from requests import Response

BASE_URL = "https://jsonplaceholder.typicode.com"
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

DEFAULT_HEADERS = {
    "User-Agent": "PyPortfolio/1.0 (+learning-requests)"
}

def http_get_json(
    path: str,
    params: Optional[Dict[str, Any]] = None,
    timeout: float = 5.0,
) -> Any:
    """
    Делает GET к BASE_URL+path, возвращает разобранный JSON (dict/list).
    Бросает дружелюбные исключения при сетевых/HTTP/JSON ошибках.
    """
    url = f"{BASE_URL}{path}"
    try:
        resp: Response = requests.get(
            url, params=params, headers=DEFAULT_HEADERS, timeout=timeout
        )
        resp.raise_for_status()             # HTTP 4xx/5xx -> исключение
        try:
            return resp.json()
        except requests.exceptions.JSONDecodeError:
            # Если сервер вернул не-JSON:
            snippet = resp.text[:200]
            raise ValueError(f"Не удалось разобрать JSON. Фрагмент ответа: {snippet!r}")
    except requests.exceptions.Timeout:
        raise TimeoutError(f"Таймаут при GET {url} (timeout={timeout}s)")
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"Проблема соединения для {url}: {e}")
    except requests.exceptions.HTTPError as e:
        # Включим немного контекста
        status = resp.status_code if 'resp' in locals() else "unknown"
        raise RuntimeError(f"HTTP ошибка {status} для {url}: {e}") from e


def save_json(obj: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def demo():
    # 1) Все посты
    posts = http_get_json("/posts")
    print(f"Всего постов: {len(posts)}")
    save_json(posts, DATA_DIR / "posts_all.json")

    # 2) Посты конкретного пользователя (query params)
    user_posts = http_get_json("/posts", params={"userId": 1})
    print(f"Постов у userId=1: {len(user_posts)}")
    save_json(user_posts, DATA_DIR / "posts_user_1.json")

    # 3) Конкретный пост и его комментарии (nested route)
    post = http_get_json("/posts/1")
    comments = http_get_json("/posts/1/comments")
    print(f"Пост #1: {post['title']!r}, комментариев: {len(comments)}")
    save_json({"post": post, "comments": comments}, DATA_DIR / "post_1_with_comments.json")

    # 4) Все имена пользователей
    users_name = http_get_json("/users")
    for i, u in enumerate(users_name, start=1):
        # безопасно берем поле 'name'
        name = u.get("username")
        print(f"{i}. {name}")
    save_json(posts, DATA_DIR / "users_name.json")

if __name__ == "__main__":
    demo()
