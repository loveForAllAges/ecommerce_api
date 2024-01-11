import stripe

import os


stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


def get_stripe_session(request, items):
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': i.currency,
                'product_data': {
                    'name': i.name,
                    'description': i.description,
                },
                'unit_amount': int(i.price * 100),
            },
            'quantity': 1,
        } for i in items],
        mode='payment',
        success_url=request.build_absolute_uri('success'),
    )
