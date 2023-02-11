import stripe
from django.http import JsonResponse, Http404
from django.views.generic import TemplateView

from django_stripe import settings

from django_stripe.base_view import BaseView
from stripe_app.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY




class ItemBuy(BaseView):
    def post(self, request, *args, **kwargs):
        item = Item.objects.filter(id=kwargs.get('id')).first()
        if not item:
            raise Http404
        checkout_session = stripe.checkout.Session.create(
            success_url='http://localhost:8000/success',
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description
                        }
                    },
                    'quantity': 1
                }
            ],
            mode='payment'
        )
        return JsonResponse({'id': checkout_session['id']})
