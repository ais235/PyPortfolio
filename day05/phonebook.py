phonebook = {}

while True:
    print("\nТелефонная книга:")
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Показать все")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Имя: ")
        phone = input("Номер: ")
        phonebook[name] = phone
        print("Контакт добавлен")

    elif choice == "2":
        name = input("Введите имя: ")
        print("Номер:", phonebook.get(name, "Не найден"))

    elif choice == "3":
        for name, phone in phonebook.items():
            print(name, ":", phone)

    elif choice == "4":
        break

    else:
        print("Неверный выбор!")
