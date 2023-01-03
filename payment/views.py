from django.shortcuts import render
from .constants import PaymentStatus
from .models import Payment
import razorpay
from django.contrib.auth.decorators import login_required
from scisoc.settings import (
    RAZORPAY_KEY_ID,
    RAZORPAY_KEY_SECRET,
)
from django.views.decorators.csrf import csrf_exempt
import json
from anastomosis.models import registration
from edc.models import Registration,RegisterWS
from medquiz import models
from insight.models import RegisterEvent,RegisterWorkshop

# Create your views here.

@login_required(login_url='/user/loginpage')
def paypage(request,amount,modelname,uid):
    user = request.user
    client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
    razorpay_order = client.order.create(
        {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
    )
    order = Payment.objects.create(
        user=user, amount=amount, modelname=modelname, uid=uid, provider_order_id=razorpay_order["id"]
    )
    order.save()
    return render(
        request,
        'payment/payment.html',
        {
            "callback_url": "http://" + "127.0.0.1:8000" + "/payment/callback/",
            "razorpay_key": RAZORPAY_KEY_ID,
            "order": order,
        },
    )


@csrf_exempt
def callback(request):

    def update_registration(payment_id):
        payment = Payment.objects.get(payment_id=payment_id)
        mname = payment.modelname
        uid = payment.uid
        if mname=="anastomosis":
            reg = registration.objects.get(reg_id=uid)
            reg.pay_id = payment_id
            reg.payment = payment
            reg.registered = True
            reg.save()
        elif mname=="hackathon":
            reg = Registration.objects.get(reg_id=uid)
            reg.pay_id = payment_id
            reg.payment = payment
            reg.save()
        elif mname=="bioworkshop":
            reg = RegisterWS.objects.get(reg_id=uid)
            reg.pay_id = payment_id
            reg.payment = payment
            reg.save()
        elif mname=="medquiz":
            reg = models.Registration.objects.get(reg_id=uid)
            reg.pay_id = payment_id
            reg.payment = payment
            reg.registered = True
            reg.save()
        elif mname=="event":
            reg = RegisterEvent.objects.get(reg_id=uid)
            reg.pay_id = payment_id
            reg.payment = payment
            reg.save()
        elif mname=="workshop":
            reg = RegisterWorkshop.objects.get(reg_id=uid)
            reg.pay_id = payment_id
            reg.payment = payment
            reg.save()

    def verify_signature(response_data):
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Payment.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            update_registration(payment_id)
            return render(request, "callback.html", {"status": order.status})
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "callback.html", {"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Payment.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "callback.html", {"status": order.status})