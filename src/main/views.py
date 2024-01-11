from typing import Any

from django.views import View, generic
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

import os

from .models import Item, Order
from .utils import get_stripe_session


class StripePublicKeyMixin():
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['stripe_public_key'] = os.environ.get('STRIPE_PUBLIC_KEY')
        return context


class ItemDetailView(StripePublicKeyMixin, generic.DetailView):
    model = Item


class BuyView(View):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs.get('pk'))

        session = get_stripe_session(request, [item])
        return JsonResponse({'session_id': session.id})


class OrderView(StripePublicKeyMixin, generic.DetailView):
    model = Order


class OrderBuyView(View):
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=kwargs.get('pk'))
        session = get_stripe_session(request, order.items.all())
        return JsonResponse({'session_id': session.id})


def success(request):
    return HttpResponse('Заказ успешно оплачен!')
