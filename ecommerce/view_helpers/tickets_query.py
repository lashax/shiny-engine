from ecommerce.models import Order
from user.models import User


def get_ticket_queryset(query: str, user: User) -> list:
    """
    Given query, return all ticket objects matching the query result
    for given user.
    """
    queryset = []
    queries = query.split()
    for q in queries:
        tickets = Order.objects.filter(user=user, ticket__name__icontains=q)

        for ticket in tickets:
            queryset.append(ticket)

    return list(set(queryset))
