from django.shortcuts import render

from .models import Dvd

# Create your views here.
def index(request):
    dvd_list = Dvd.objects.all()
    return render(request, 'dvds/index.html', { 'dvds':dvd_list })
