from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Offer
from django.shortcuts import render
from django.core import serializers
from django.utils.safestring import mark_safe
import json


def index(request):
    all_offers = Offer.objects.all()
    context = {'all_offers': all_offers}
    return render(request, 'offers/index.html', context)


def room(request, room_name):
    return render(request, 'offers/notification.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
