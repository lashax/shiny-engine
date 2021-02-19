from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ecommerce.forms import OrderTicket
from .models import Ticket, Order
from .view_helpers import generate_hash


TICKET_PRICE = 20


def home(request: WSGIRequest) -> HttpResponse:
    week = Order.objects.filter(order_time__week=
                                datetime.now().isocalendar()[1],
                                user=request.user)
    month = Order.objects.filter(order_time__month=
                                 datetime.now().month, user=request.user)
    year = Order.objects.filter(order_time__year=
                                datetime.now().year, user=request.user)

    stats = [week.count(), month.count(), year.count(),
             week.count()*TICKET_PRICE, month.count()*TICKET_PRICE,
             year.count()*TICKET_PRICE]

    if request.method == 'POST':
        form = OrderTicket(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            hash_code = generate_hash.generation()
            t = Ticket(name=order.name, start_time=order.start_time,
                       end_time=order.end_time, hash_code=hash_code)
            t.save()
            order.ticket = t
            order.user = request.user
            order.save()
            return redirect('home')
    else:
        form = OrderTicket()

    return render(request, 'ecommerce/home.html', {'form': form,
                                                   'stats': stats})


@login_required
def tickets(request: WSGIRequest) -> HttpResponse:
    paginator = Paginator(Ticket.objects.all(), 3,
                          allow_empty_first_page=True)
    page_number = request.GET.get('page')
    ticket_page = paginator.get_page(page_number)

    return render(request, 'ecommerce/tickets.html',
                  {'ticket_page': ticket_page})
