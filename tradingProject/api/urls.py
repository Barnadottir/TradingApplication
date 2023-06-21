from django.urls import path
from .views import PostList,StockDataView,accountDataAlpaca,StockDataYFinance

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('stockdata/', StockDataView.as_view()),
    path('accountData/',accountDataAlpaca.as_view()),
    path('BTCData/',StockDataYFinance.as_view()),
]
