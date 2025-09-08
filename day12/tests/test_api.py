import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_post():
    payload = {"userId": 1, "title": "API Test", "body": "Learning tests"}
    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == payload["title"]
    assert "id" in data


def test_get_post():
    resp = requests.get(f"{BASE_URL}/posts/1")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
    assert "title" in data


def test_update_post():
    payload = {"id": 1, "userId": 1, "title": "Updated", "body": "Changed"}
    resp = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Updated"


def test_patch_post():
    payload = {"title": "Partially updated"}
    resp = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Partially updated"


def test_delete_post():
    resp = requests.delete(f"{BASE_URL}/posts/1")
    assert resp.status_code in (200, 204)
