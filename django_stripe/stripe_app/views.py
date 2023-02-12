import stripe
from django.http import Http404
from django.views.generic import TemplateView

from django_stripe import settings
from django_stripe.base_view import BaseView
from stripe_app.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessBuy(TemplateView):
    template_name = 'success_buy.html'


class ItemDetail(TemplateView):
    template_name = 'item_detail.html'

    def get_context_data(self, **kwargs):
        # if not found item return 404 error
        item = Item.objects.filter(id=kwargs.get('id')).first()
        if not item:
            raise Http404
        context = super().get_context_data(**kwargs)
        context.update({
            "item": item,
            'STRIPE_PUBLISH_KEY': settings.STRIPE_PUBLISH_KEY
        })
        return context


class ItemBuy(BaseView):
    def get(self, request, *args, **kwargs):
        # if not found item return 404 error
        item = Item.objects.filter(id=kwargs.get('id')).first()
        if not item:
            raise Http404
        success_url = f'{request.build_absolute_uri("/")}success'
        checkout_session = stripe.checkout.Session.create(
            success_url=success_url,
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
        return {'id': checkout_session['id']}
