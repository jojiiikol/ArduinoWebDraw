from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import ArduinoMatrixSerializer


class MyView(APIView):
    def get(self, request, *args, **kwargs):
        matrix = Matrix.objects.all().order_by('-id').first()
        serializer = ArduinoMatrixSerializer(matrix)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArduinoMatrixSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DrawImageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main.html'
    def get(self, request, *args, **kwargs):
        return Response({'data': None})

