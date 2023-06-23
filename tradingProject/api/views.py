from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from django.views import View
from .scripts.basicTestScript import testScript
from .services import AlpacaApi,YFinanceApi

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class StockDataView(View):
    
    def get(self, request, *args, **kwargs):
        data = testScript()  # Call the testScript function here
        #data = {
        #    'company': 'Apple Inc.',
        #    'ticker': 'AAPL',
        #    'price': '150.00 USD'
        #}
        return JsonResponse(data, safe=False) 
    

#This should be in its own file eventually

class accountDataAlpaca(View):
    def get(self,request,*args,**kwargs):
        api = AlpacaApi()
        data = api.get_account_info()
        #return
        return JsonResponse(data,safe = False)

class StockDataYFinance(View):
    def get(self,request,*args,**kwargs):
        api = YFinanceApi()
        data = api.get_BTC_Trading_Data()
        return JsonResponse(data,safe = False)

class MakeTradeView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        api = AlpacaApi()
        trade = api.make_trade(data['symbol'], data['shares'], data['side'])
        return JsonResponse(trade, safe=False)