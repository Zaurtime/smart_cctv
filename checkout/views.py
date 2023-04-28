from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N1onrA0Bi8wCwZZkbTjo5if6gRrYH5jkSrBLMcQGYFG6a32iyli6TEvaxdnA9pGkyIG2HuXuQFAMJMR1l1rC02o00WZr6Mem7',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)