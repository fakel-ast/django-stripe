import stripe
from django.http import JsonResponse

from django_stripe import settings

from django_stripe.base_view import BaseView
from stripe_app.schemas import ItemBuySchemas

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemBuy(BaseView):
    schema = ItemBuySchemas

    def post(self, request, *args, **kwargs):
        item_data: ItemBuySchemas = self.parse_schemas()
        checkout_session = stripe.checkout.Session.create(
            success_url='http://localhost:8000/success',
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item_data.price,
                        'product_data': {
                            'name': item_data.name,
                            'description': item_data.description
                        }
                    },
                    'quantity': 1
                }
            ],
            mode='payment'
        )
        return JsonResponse({'id': checkout_session['id']})
