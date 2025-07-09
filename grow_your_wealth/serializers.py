from rest_framework import serializers
from .models import Investment, InvestmentGrowth

class InvestmentGrowthSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentGrowth
        fields = ['id', 'year', 'month', 'interest', 'updated_capital', 'created_at']

class InvestmentSerializer(serializers.ModelSerializer):
    wealth_growth = InvestmentGrowthSerializer(many=True, read_only=True)  # related_name from FK

    class Meta:
        model = Investment
        fields = ['id', 'name', 'initial_amount', 'top_up', 'interest_rate', 'duration_in_years',
                  'topup_frequency', 'company', 'created_at', 'wealth_growth']