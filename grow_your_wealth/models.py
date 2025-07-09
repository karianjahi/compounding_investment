from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Investment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    initial_amount = models.DecimalField(max_digits=20, decimal_places=2)
    top_up = models.DecimalField(default=250_000, max_digits=20, decimal_places=2)
    interest_rate = models.DecimalField(default=0.15, max_digits=5, decimal_places=2, help_text="decimal point between 0 and 1 with only 2 decimal places allowed")
    duration_in_years = models.IntegerField(default=10, help_text="integer")
    topup_frequency = models.CharField(max_length=20, default="month", help_text="Defaults to month for now")
    company = models.CharField(max_length=50, default="Mansa-X", help_text="name of company. Optional field")
    name = models.CharField(max_length=100, help_text="investment name e.g. retirement")
        
    

    def __str__(self):
        return f'Invested {self.initial_amount} within {self.name} scheme'

class InvestmentGrowth(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='wealth_growth')
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    interest = models.DecimalField(max_digits=20, decimal_places=2)
    updated_capital = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = "Investment Growth Record"
        verbose_name_plural = "Investment Growth Records"
        unique_together = ("investment", "year", "month")
        ordering = ["year", "month"]

    def __str__(self):
        return f"{self.investment.name}: {self.year}/{self.month}"

