def ticket_message(count_function):
    def wrapper():
        gen = count_function()  # Create generator object
        print("Your ticket number is:")
        ticket = next(gen)  # Get first ticket
        while True:
            yield ticket
            print("Someone will be with you soon")
            ticket = next(gen)  # Get the next ticket

    return wrapper


@ticket_message
def perfume_count():
    ticket = 1
    while True:
        yield "P-" + str(ticket)
        ticket += 1


increment_perfume = perfume_count()
print(next(increment_perfume))
print(next(increment_perfume))
print(next(increment_perfume))
