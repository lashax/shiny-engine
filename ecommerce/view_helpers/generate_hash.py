from random import randint

from ecommerce.models import Ticket


def generation() -> str:
    """Generates 50 characters length hash_code to be used for a ticket."""
    while True:
        hash_code = ''
        for i in range(50):
            hash_code += chr(randint(48, 122))

        tickets = Ticket.objects.all()
        to_continue = False

        for ticket in tickets:
            if ticket.hash_code == hash_code:
                to_continue = True
        if to_continue:
            continue

        break

    return hash_code
