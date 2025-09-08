import pytest
import requests

# Общая константа для всех тестов
BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url():
    """Фикстура для базового URL API"""
    return BASE_URL


@pytest.fixture(scope="session")
def session():
    """
    Фикстура для requests.Session()
    Использует одно соединение для всех тестов → быстрее и чище
    """
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json; charset=UTF-8"})
    yield s
    s.close()
