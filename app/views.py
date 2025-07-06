from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class IntroClass(APIView):

    def get(self, request):
        return Response({"msg":f"hello {request.query_params.get('name')}! this is from production"})