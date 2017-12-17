from django.shortcuts import render
from .models import Insurance1

def insurance(request):
    return render(request, 'insurance/insurance.html')


def insurance1(request, pk_ins):
    pk_insurance = pk_ins
    return render(request, 'insurance/insuranceM.html', {'pk_ins': pk_insurance})


def insurance_type(request, type_insurance):
    ins_type = ''
    try:
        ins_type = Insurance1.objects.filter(insurance_type=type_insurance).last()
    except Exception as e:
        pass
    return render(request, 'insurance/insurance_type.html', {'ins_type': ins_type})
