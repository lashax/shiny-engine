from django.forms import ModelForm

from ecommerce.models import Order


class OrderTicket(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'start_time', 'end_time']
