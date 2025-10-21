num_tickets = 237  # количество проданных билетов
bus_capacity = 48  # количество мест в автобусе

num_bus = num_tickets // bus_capacity
num_left_passengers = num_tickets % bus_capacity

print(num_bus, num_left_passengers)
