def calculate_delivery(subtotal, express=False):
    if isinstance(subtotal, bool) or not isinstance(subtotal, int):
        raise TypeError("Сумма заказа должна быть целым числом")
    if not isinstance(express, bool):
        raise TypeError("Файл экспресс-доставки должен быт логическим (True/Fallse)")

    if subtotal < 0:
        raise ValueError("Сумма заказа не может быть отрицательной")

    if subtotal < 1000:
        cost = 400
    elif 100 <= subtotal < 5000:
        cost = 150
    else:
        cost = 0
    if express:
        cost += 250

    return cost
