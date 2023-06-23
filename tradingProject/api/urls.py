from django.urls import path
from .views import PostList,StockDataView,accountDataAlpaca,StockDataYFinance,MakeTradeView

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('stockdata/', StockDataView.as_view()),
    path('accountData/',accountDataAlpaca.as_view()),
    path('BTCData/',StockDataYFinance.as_view()),
    path('makeTrade/', MakeTradeView.as_view()),
]
