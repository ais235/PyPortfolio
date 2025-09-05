#!/usr/bin/env python3
"""
Mini exercises for Day 10:
- GET /users -> print all user names
- GET /todos?userId=2 -> count completed == True
- GET /photos?albumId=1 -> save JSON to day10/data/photos_album_1.json
"""
from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, Optional
import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def http_get_json(path: str, params: Optional[Dict[str, Any]] = None, timeout: float = 5.0) -> Any:
    """
    GET BASE_URL + path, return parsed JSON (list/dict).
    Raises exceptions on network/HTTP/JSON errors with readable messages.
    """
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.get(url, params=params, timeout=timeout, headers={"User-Agent": "mini-exercises/1.0"})
        resp.raise_for_status()  # raise HTTPError for 4xx/5xx
    except requests.exceptions.Timeout:
        raise TimeoutError(f"Timeout when requesting {url} (timeout={timeout}s)")
    except requests.exceptions.ConnectionError as e:
        raise ConnectionError(f"Connection error when requesting {url}: {e}")
    except requests.exceptions.HTTPError as e:
        # include status code for clarity
        raise RuntimeError(f"HTTP error {resp.status_code} for {url}: {e}") from e

    try:
        return resp.json()
    except ValueError:
        snippet = resp.text[:300]
        raise ValueError(f"Response from {url} is not valid JSON. Snippet: {snippet!r}")


def save_json(obj: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def exercise_users_print_names() -> None:
    """Получаем всех пользователей и печатаем их имена."""
    users = http_get_json("/users")
    if not isinstance(users, list):
        raise RuntimeError("Ожидали список пользователей")
    print("Список имён пользователей:")
    for i, u in enumerate(users, start=1):
        # безопасно берем поле 'name'
        name = u.get("name", "<no name>")
        print(f"{i}. {name}")


def exercise_todos_count_completed(user_id: int = 2) -> int:
    """Получаем todos для userId и считаем completed == True."""
    todos = http_get_json("/todos", params={"userId": user_id})
    if not isinstance(todos, list):
        raise RuntimeError("Ожидали список todo")
    completed_count = sum(1 for t in todos if bool(t.get("completed")))
    print(f"UserId={user_id}: всего задач {len(todos)}, выполнено (completed==true): {completed_count}")
    return completed_count


def exercise_photos_save(album_id: int = 1) -> Path:
    """Получаем фото для albumId и сохраняем их метаданные в JSON."""
    photos = http_get_json("/photos", params={"albumId": album_id})
    if not isinstance(photos, list):
        raise RuntimeError("Ожидали список фото")
    out_path = DATA_DIR / f"photos_album_{album_id}.json"
    save_json(photos, out_path)
    print(f"Сохранено {len(photos)} фото в {out_path}")
    return out_path


def main() -> None:
    try:
        exercise_users_print_names()
        print()
        exercise_todos_count_completed(user_id=2)
        print()
        exercise_photos_save(album_id=1)
    except Exception as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
