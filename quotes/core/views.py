from django.shortcuts import render
from rest_framework.views import APIView
from . models import React
from rest_framework.response import Response
from .serializers import ReactSerializer


class ReactView(APIView):
    serializer_class = ReactSerializer
    def get(self, request):
        detail = [ {"name": detail.name,"detail": detail.detail}
        for detail in React.objects.all()]
        return Response(detail)


    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)