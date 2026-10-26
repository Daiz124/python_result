# # Ввод
# login = input("Логин: ")
# password = input("Пароль: ")

# # Проверка
# if login == "student":
#     if password == "python2026":
#         print("Добро пожаловать")
#     else:
#         print("Неверный пароль")
# else:
#     print("Пользователь не найден")

#     # Ввод
# balance = int(input("Баланс, руб.: "))
# amount = int(input("Сумма, руб.: "))

# # Проверка
# if amount % 100 == 0:
#     if amount <= balance:
#         notes = amount // 100
#         balance -= amount
#         print("Купюр выдано:", notes)
#         print("Остаток:", balance, "руб.")
#     else:
#         print("Недостаточно средств")
# else:
#     print("Сумма должна быть кратна 100")

#     # Ввод
# day = int(input("День недели (1-7): "))
# age = int(input("Возраст: "))

# # Выбор цены
# if day <= 5:
#     print("Будний день")
#     if age < 7:
#         price = 0
#     else:
#         price = 300
# else:
#     print("Выходной день")
#     if age < 7:
#         price = 100
#     elif age < 18:
#         price = 250
#     else:
#         price = 500

# # Вывод
# print("Цена билета:", price, "руб.")

#1
# price = 50
# karta = input("Приложена ли карта?: ")
# balance = float(input("Баланс карты: "))
# if karta == "да":
#     if balance >= 50:
#         print("Проходите")
#     else:
#         print("Недостаточно средств")
# else:
#     print("Приложите карту")


#2
# zona = input("входит ли адрес в зону? ")
# summa = float(input("Сумма заказа: "))
# if zona == "да":
#     if summa >= 800:
#         print("Доставка бесплатная")
#     else:
#         print("Доставка 150 руб.")
# else:
#     print("По этому адресу не доставляем")




tovari = int(input("Введите кол-во товаров: "))
if tovari > 0 and tovari % 2 ==0:
    print("Заказ принят")
elif tovari > 0 and not tovari % 2 ==0:
    print("Товар продаётся парами")
else:
    print("Количество должно быть больше нуля")