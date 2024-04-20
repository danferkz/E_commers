from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'app1/index.html')

def api_endpoint(request):
    data = {
        'message': 'This is an API endpoint for app1',
        'status': 'success'
    }
    return JsonResponse(data)