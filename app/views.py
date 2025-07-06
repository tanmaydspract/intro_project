from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class IntroClass(APIView):

    def get(self, request):
        if not request.query_params.get('name'):
            return Response({'msg':'please provied name'})
        if not request.query_params.get('a1') or not request.query_params.get('a2'):
            return Response({"msg":f"hello {request.query_params.get('name')}!! this is from production, you have not provided calculation data"})    
        return Response({"msg":f"hello {request.query_params.get('name')}!! this is from production, your calculation : {str(int(request.query_params.get('a1'))+int(request.query_params.get('a2')))}"})