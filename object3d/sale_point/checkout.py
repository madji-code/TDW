from django.shortcuts import HttpResponse, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Product
import stripe
 
stripe.api_key = settings.STRIPE_SECRET_KEY
 
 
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=self.kwargs["pk"])
        domain = "https://3dw.madji.org"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'cad',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                            'images': [product.image]
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id,
            },
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)
    

class SuccessView(TemplateView):
    template_name = "sale_point/success.html"
 
class CancelView(TemplateView):
    template_name = "sale_point/cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "sale_point/landing.html"
 
    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
        })
        return context
    

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
        event['data']['object']['id'],
        expand=['line_items'],
        )
        complete_order(session)

    # Passed signature verification
    return HttpResponse(status=200)

def complete_order(session):
    customer_email = session['customer_details']['email']
    product_id = session['metadata']['product_id']

    product = Product.objects.get(id=product_id)

    send_mail(
        subject = 'That’s your subject',
        message = 'That’s your message body',
        from_email = 'madji.corp@gmail.com',
        recipient_list = [customer_email],
        fail_silently = False,
    )