from django.http import HttpResponse

def index(request):
    return HttpResponse ("page d'index.")
# Create your views here.
