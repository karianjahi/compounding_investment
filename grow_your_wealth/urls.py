from django.urls import path
from .views import (
    InvestmentList, 
    InvestmentDetail,
    InvestmentGrowthList,
    InvestmentGrowthDetail,
    InvestmentGrowthBulkCreate,
)

urlpatterns = [
    path("investments", InvestmentList.as_view(), name="investment-list"),
    path("investments/<int:pk>", InvestmentDetail.as_view(), name="investment-detail"),
    # path("records", InvestmentGrowthList.as_view(), name="record-list"),
    # path("records/<int:pk>", InvestmentGrowthDetail.as_view(), name="record-detail"),
    # path("investmentgrowth/bulk/", InvestmentGrowthBulkCreate.as_view())
]