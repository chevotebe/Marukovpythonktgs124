number = int(input("Введите число:"))
if number in [7, 13, 21]:
print("Счастливое число!")
elif number in range(1 , 101):
print("Число в указанном диапазоне")
else:
print("Не повезло")




is_logged_in = True
has_items_in_cart = True
has_shipping_address = False
has_order = False
if is_logged_in and has_items_in_cart and has_shipping_address and has_order:
    print("Все критерии для оформления заказа выполнены. Заказ может быть оформлен")
else:
    print("Не все критерии для оформления заказа выполнены. Пожалуйста, проверьте информацию")
user_first_order = True
order_cost = 1500

if user_first_order or order_cost > 1000:
    print("Вы получаете скидку!")
else:
    print("Скидка не доступна.")