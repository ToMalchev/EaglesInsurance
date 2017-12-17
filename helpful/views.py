from django.shortcuts import render
from helpful.models import helpful

def helpful_1(request):
    helpful_L = helpful.objects.all()
    return render(request, 'helpful/helpful.html', {'item': helpful_L})
