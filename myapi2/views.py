from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import requests

@api_view(["GET"])
def Resources(request):
    try:
        server = request.query_params["serverid"]
        cpu = int(request.query_params["cpu"])
        memory = int(request.query_params["memory"])
        disk = int(request.query_params["disk"])

        if (cpu>85 and memory>75 and disk>60): return Response("No Alert, "+server)
        elif (cpu>85 and memory>75 and disk<60): return Response("Alert, "+server+"DISK_UTLIZATION_VIOLATED")
        elif (cpu>85 and memory<75 and disk>60): return Response("Alert, "+server+"MEMORY_UTLIZATION_VIOLATED")
        elif (cpu>85 and memory<75 and disk<60): return Response("Alert, "+server+"MEMORY_UTLIZATION_VIOLATED, DISK_UTLIZATION_VIOLATED")
        elif (cpu<85 and memory>75 and disk>60): return Response("Alert, "+server+"CPU_UTILIZATION_VIOLATED")
        elif (cpu<85 and memory<75 and disk>60): return Response("Alert, "+server+"CPU_UTILIZATION_VIOLATED,MEMORY_UTILIZATION VIOLATED")
        elif (cpu<85 and memory<75 and disk<60): return Response("Alert, "+server+"CPU_UTILIZATION_VIOLATED,MEMORY_UTILIZATION VIOLATED, DISK_UTLIZATION_VIOLATED")
        else: return Response("Alert, "+server+"CPU_UTILIZATION_VIOLATED,DISK_UTLIZATION_VIOLATED")

    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
