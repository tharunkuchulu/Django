from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

def sample_get_view(request):
    return HttpResponse("Hello World",content_type="text/plain")   

def sample1(request):
    return JsonResponse({"message":"Hello JSON"}) 

