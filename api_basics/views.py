from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls.base import clear_script_prefix
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Articles
from .serializers import ArticleSerializer
# Create your views here.

@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles =Articles.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
            
        return JsonResponse(serializer.errors, status=400)