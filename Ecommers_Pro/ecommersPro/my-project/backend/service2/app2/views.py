from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'app2/index.html')

def api_endpoint(request):
    # Your API logic here
    data = {
        'message': 'This is an example API endpoint in app2',
        'status': 'success'
    }
    return JsonResponse(data)