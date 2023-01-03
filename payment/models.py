from django.db import models
from .constants import PaymentStatus
from django.contrib.auth.models import User

# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False)
    amount = models.FloatField("Amount", null=False, blank=False)
    modelname = models.CharField(max_length=50)
    uid = models.UUIDField(null=False,blank=False)
    status = models.CharField("Payment Status",default=PaymentStatus.PENDING,max_length=275,null=False,blank=False)
    provider_order_id = models.CharField("Order ID", max_length=50, null=False, blank=False)
    payment_id = models.CharField("Payment ID", max_length=50, null=False, blank=False)
    signature_id = models.CharField("Signature ID", max_length=150, null=False, blank=False)

    def __str__(self):
        return f"{self.id}-{self.user.first_name}-{self.status}"