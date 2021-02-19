from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from ecommerce.forms import OrderTicket
from .models import Ticket
from .view_helpers import generate_hash


def home(request: WSGIRequest) -> HttpResponse:
    if request.method == 'POST':
        form = OrderTicket(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            hash_code = generate_hash.generation()
            t = Ticket(start_time=order.start_time,
                                  end_time=order.end_time, hash_code=hash_code)
            t.save()
            order.ticket = t
            order.save()
            return redirect('home')
    else:
        form = OrderTicket()
    return render(request, 'ecommerce/home.html', {'form': form})
