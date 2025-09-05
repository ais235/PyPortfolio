import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"


def create_post(user_id: int, title: str, body: str):
    url = f"{BASE_URL}/posts"
    payload = {
        "userId": user_id,
        "title": title,
        "body": body,
    }
    headers = {"Content-Type": "application/json; charset=UTF-8"}

    resp = requests.post(url, json=payload, headers=headers, timeout=5)
    print("Статус-код:", resp.status_code)

    # Проверка статуса
    if resp.status_code == 201:
        print("✅ Пост успешно создан (фейково).")
    else:
        print("⚠️ Что-то пошло не так.")

    try:
        data = resp.json()
        print("Ответ сервера:\n", json.dumps(data, indent=2, ensure_ascii=False))
        return data
    except ValueError:
        print("Ответ не JSON:", resp.text)
        return None

def create_comments(post_id: int, name: str, email: str, body: str):
    url = f"{BASE_URL}/comments"
    payload = {
        "postId": post_id,
        "name": name,
        "email": email,
        "body": body
    }
    headers = {"Content-Type": "application/json; charset=UTF-8"}

    resp = requests.post(url, json=payload, headers=headers, timeout=5)
    print("Статус-код:", resp.status_code)

    # Проверка статуса
    if resp.status_code == 201:
        print("✅ Комментарий добавлен (фейково).")
    else:
        print("⚠️ Что-то пошло не так.")

    try:
        data = resp.json()
        print("Ответ сервера:\n", json.dumps(data, indent=2, ensure_ascii=False))
        return data
    except ValueError:
        print("Ответ не JSON:", resp.text)
        return None

if __name__ == "__main__":
    create_post(
        user_id=1,
        title="Мой первый пост через API",
        body="Сегодня я учусь делать POST-запросы в Python 🚀",
    )
