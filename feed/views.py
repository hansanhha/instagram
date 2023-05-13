from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class Feed(APIView):

    def get(self, request):
        return render(request, '../instagram/../templates/feed/main.html')

    def post(self, request):
        return render(request, '../instagram/../templates/feed/main.html')