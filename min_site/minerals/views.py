from django.http import HttpResponse
from django.shortcuts import render

from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    output = ', '.join([str(mineral) for mineral in minerals])
    return HttpResponse(output)
