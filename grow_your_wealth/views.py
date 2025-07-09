from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Investment, InvestmentGrowth
from rest_framework import generics
from .models import Investment, InvestmentGrowth
from .serializers import InvestmentSerializer, InvestmentGrowthSerializer
from .calculator import get_growth_records

# Create your views here.
class InvestmentList(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Update the investment first
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Recalculate growth after update
        instance.refresh_from_db()
        growth_data = get_growth_records(instance)  # this returns list of dicts
        
        # Clear old growth data (optional but recommended for update case)
        # InvestmentGrowth.objects.filter(investment=instance).delete()
        
        # Save new growth data
        for entry in growth_data:
            InvestmentGrowth.objects.create(
                investment=instance,
                year=entry['year'],
                month=entry['month'],
                interest=entry['interest'],
                updated_capital=entry['capital_gains']
            )

        return Response(serializer.data)

class InvestmentGrowthList(generics.ListCreateAPIView):
    queryset = InvestmentGrowth.objects.all()
    serializer_class = InvestmentGrowthSerializer

class InvestmentGrowthDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvestmentGrowth.objects.all()
    serializer_class = InvestmentGrowthSerializer


class InvestmentGrowthBulkCreate(APIView):
    def post(self, request, *args, **kwargs):
        investment_id = request.data.get("investment_id")
        records = request.data.get("records", [])

        try:
            investment = Investment.objects.get(id=investment_id)
        except Investment.DoesNotExist:
            return Response({"error": "Investment not found"}, status=status.HTTP_404_NOT_FOUND)

        objs = [
            InvestmentGrowth(
                investment=investment,
                year=r["year"],
                month=r["month"],
                interest=r["interest"],
                capital_gains=r["capital_gains"]
            )
            for r in records
        ]

        InvestmentGrowth.objects.bulk_create(objs)
        return Response({"message": f"{len(objs)} records created."}, status=status.HTTP_201_CREATED)
