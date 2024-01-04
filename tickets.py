# handle ticketing for perfume department
def perfume_ticket():
    ticket = 1
    while True:
        yield "P-" + str(ticket)
        ticket += 1


p = perfume_ticket()


# handle ticketing for medicine department
def medicine_ticket():
    ticket = 1
    while True:
        yield "M-" + str(ticket)
        ticket += 1


m = medicine_ticket()


# handle ticketing for cosmetic department
def cosmetic_ticket():
    ticket = 1
    while True:
        yield "C-" + str(ticket)
        ticket += 1


c = cosmetic_ticket()


# ticket decorator
def decorator(product):
    print("\n" + "*" * 20)
    print("Your number is: ")

    if product == "P":
        print(next(p))
    elif product == "M":
        print(next(m))
    else:
        print(next(c))

    print("Please wait for your tuen")
    print("\n" + "*" * 20)
