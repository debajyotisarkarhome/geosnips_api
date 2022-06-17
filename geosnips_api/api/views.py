import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import features, properties, geometry
from .serializer import FeatureSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def Create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeatureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=409)
    return HttpResponse(status=405)

@csrf_exempt
def Read(request):
    if request.method == 'GET':
        features_list = features.objects.all()
        serializer = FeatureSerializer(features_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(status=405)

@csrf_exempt
def Update(request):
    try:
        selectedFeature = properties.objects.get(pk=json.loads(request.body)['properties']['id'])
    except features.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'POST':
        selectedFeature.delete()
        data = JSONParser().parse(request)
        serializer = FeatureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse(status=400)

@csrf_exempt
def Delete(request):
    try:
        selectedFeature = properties.objects.get(pk=json.loads(request.body)['properties']['id'])
    except:
        return HttpResponse(status=404)
    if request.method == 'DELETE':
        selectedFeature.delete()
        return HttpResponse(status=204)
