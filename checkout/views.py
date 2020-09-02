from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing is your bag at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
       'order_form': order_form,
       'stripe_public_key': 'pk_test_51HMevpF3StHkhbsY4dtTWM8bedI1tpFheIP2FN3D38ehS5rC7wvog4c0O4DJMgqSMCRdWE3mq7fTEyftw72xaCBC007LMNc8uN',
       'client_secret': 'test client secret',
    }

    return render(request, template, context)
