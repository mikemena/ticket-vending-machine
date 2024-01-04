# ticket decorator
def ticket_message(count_function):
    def wrapper():
        print("Your ticket number is:")
        yield from count_function()
        print("Someone will be with you soon")

    return wrapper


# handle ticketing for perfume department
@ticket_message
def perfume_count():
    ticket = 1
    while True:
        yield "P-" + str(ticket)
        ticket += 1


increment_perfume = perfume_count()
print(next(increment_perfume))


# handle ticketing for medicine department
@ticket_message
def medicine_count():
    ticket = 1
    while True:
        yield "M-" + str(ticket)
        ticket += 1


increment_medicine = medicine_count()
# print(next(increment_medicine))


# handle ticketing for cosmetic department
@ticket_message
def cosmetic_count():
    ticket = 1
    while True:
        yield "C-" + str(ticket)
        ticket += 1


increment_cosmetic = cosmetic_count()
# print(next(increment_cosmetic))
