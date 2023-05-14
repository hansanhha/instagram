from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed


class FeedView(APIView):

    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        return render(request, 'feed/main.html', context=dict(feed_list=feed_list))

    def post(self, request):
        return render(request, 'feed/main.html')