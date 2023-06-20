from django.urls import path
from .views import PostList,StockDataView

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('stockdata/', StockDataView.as_view()),
]
