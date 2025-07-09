from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Investment, InvestmentGrowth
from .calculator import get_growth_records

@receiver(post_save, sender=Investment)
def create_growth_records(sender, instance, created, **kwargs):
    if not created:
        return

    growth_data = get_growth_records(instance)

    records = [
        InvestmentGrowth(
            investment=instance,
            year=item['year'],
            month=item['month'],
            interest=item['interest'],
            capital_gains=item['capital_gains']
        )
        for item in growth_data
    ]
    InvestmentGrowth.objects.bulk_create(records)