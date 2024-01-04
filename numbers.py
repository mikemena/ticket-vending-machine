# perfume, medicine, cosmetics

# Your number is:
# the number is P-1, M-1, or C-1 for each dept
# Wait and someone will be with you shortly

# Use generator to give next number

# use decorator to append the number with message before and after


# handle ticketing for perfume department
def perfume_count():
    ticket = 1
    while True:
        yield "P-" + str(ticket)
        ticket += 1


increment_perfume = perfume_count()
print(next(increment_perfume))


# handle ticketing for medicine department
def medicine_count():
    ticket = 1
    while True:
        yield "M-" + str(ticket)
        ticket += 1


increment_medicine = medicine_count()
print(next(increment_medicine))


# handle ticketing for cosmetic department
def cosmetic_count():
    ticket = 1
    while True:
        yield "C-" + str(ticket)
        ticket += 1


increment_cosmetic = cosmetic_count()
print(next(increment_cosmetic))
