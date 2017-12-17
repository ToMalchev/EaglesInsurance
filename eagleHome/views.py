from django.shortcuts import render
from eagleHome.models import contact1, info

def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    contact_obj = ''
    try:
        contact_obj = contact1.objects.last()
    except Exception as e:
        pass
    return render(request, 'personal/contact.html', {'contact1': contact_obj})


def forUs(request):
    info_last = ''
    try:
        info_last = info.objects.last()
    except:
        pass
    return render(request, 'personal/info(for_us).html', {'info_last': info_last})
