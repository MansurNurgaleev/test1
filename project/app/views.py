import os

import stripe
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from app.models import Item


stripe.api_key = os.getenv('STRIPE_KEY')

class BuyView(View):

    def get(self, request, id):
        item = Item.objects.get(id=id)
        session = stripe.checkout.Session.create(
            line_items=[{
              'price_data': {
                'currency': 'usd',
                'product_data': {
                'name': item.name,
                'description': item.description
                },
                'unit_amount': int(item.price * 100),
              },
              'quantity': 1,
            }],
            mode='payment',
            success_url= request.build_absolute_uri('/success'),
            cancel_url= request.build_absolute_uri('/cancel'),)
        return JsonResponse(session, status=200)


class ItemView(View):
    def get(self, request, id):
        try:
            item = Item.objects.get(id=id)
        except:
            pass
        return render(request, 'item.html',{"item": item, "stripe_key": os.getenv('STRIPE_PKEY')})


class SuccessView(View):
    def get(self, request):
        return render(request, 'success.html', status=200)


class CancelView(View):
    def get(self, request):
        return render(request, 'cancel.html', status=200)


def view_404(request, exception=None):
    return render(request, '404.html', status=404)