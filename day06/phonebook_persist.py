# file: day06/phonebook_persist.py
from pathlib import Path
import json
import csv

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
JSON_PATH = DATA_DIR / "phonebook.json"

def load_phonebook(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            return {}
    except json.JSONDecodeError:
        print("⚠️ Файл повреждён или пуст. Начинаю с пустой книги.")
        return {}

def save_phonebook(path: Path, book: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)

def export_csv(path: Path, book: dict) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "phone"])
        for name, phone in book.items():
            writer.writerow([name, phone])

def print_menu():
    print("\nТелефонная книга:")
    print("1. Добавить/обновить контакт")
    print("2. Найти контакт")
    print("3. Показать все")
    print("4. Удалить контакт")
    print("5. Экспорт в CSV")
    print("0. Выход")

def main():
    phonebook = load_phonebook(JSON_PATH)
    print(f"Загружено контактов: {len(phonebook)}")

    while True:
        print_menu()
        choice = input("Выбор: ").strip()

        if choice == "1":
            name = input("Имя: ").strip()
            phone = input("Номер: ").strip()
            phonebook[name] = phone
            save_phonebook(JSON_PATH, phonebook)
            print("✅ Сохранено.")

        elif choice == "2":
            name = input("Имя для поиска: ").strip()
            print("Номер:", phonebook.get(name, "Не найден"))

        elif choice == "3":
            if not phonebook:
                print("Книга пуста.")
            else:
                for name, phone in sorted(phonebook.items()):
                    print(f"{name}: {phone}")

        elif choice == "4":
            name = input("Имя для удаления: ").strip()
            if name in phonebook:
                del phonebook[name]
                save_phonebook(JSON_PATH, phonebook)
                print("🗑️ Удалено и сохранено.")
            else:
                print("Контакт не найден.")

        elif choice == "5":
            csv_path = DATA_DIR / "phonebook.csv"
            export_csv(csv_path, phonebook)
            print(f"📤 Экспортировано: {csv_path}")

        elif choice == "0":
            print("Выход. До встречи!")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
