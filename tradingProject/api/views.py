from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from django.views import View
from .scripts.basicTestScript import testScript

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