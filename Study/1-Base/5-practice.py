num_tickets = 40  # количество проданных билетов
bus_capacity = 20  # количество мест в автобусе

bus_quantity = num_tickets // bus_capacity  # Кол-во полных автобусов
num_tickets_left = num_tickets % bus_capacity  # Кол-во оставшихся пассажиров

has_partial_bus = False
empty_seats = 0

if num_tickets_left:
    if num_tickets_left >= bus_quantity / 2:  # Есть ли автобусы, заполненные наполовину
        bus_quantity += 1  # Если есть, добавляю кол-во автобусов
        has_partial_bus = True  # Есть ли автобусы, заполненные наполовину

        empty_seats = bus_capacity - num_tickets_left  # Остаток свободных мест
        num_tickets_left = 0


print(bus_quantity, num_tickets_left, has_partial_bus, empty_seats)
