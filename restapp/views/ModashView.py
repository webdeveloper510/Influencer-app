from rest_framework.views import APIView
from rest_framework.response import Response
from restapp.models import *
from restapp.serializers import *
import requests
from rest_framework import generics, status
import json


headers={"Authorization": "Bearer yGrFqiK4YqDtqODbGRZkZrWRIgsjFLZP"}


#YOUTUBER FOLLOWER API
class YoutubeFollower(APIView):
    def get(self,request):
        user_handler=request.GET.get("user")
        base_url=f"https://api.modash.io/v1/youtube/profile/{user_handler}/report"
        response = requests.get(base_url, headers=headers)
        return Response({"success":json.loads(response.text)},status=status.HTTP_200_OK)
    
#INSTAGRAM FOLLOWER API
class InstagramFollower(APIView):
    def get(self,request):
        user_handler=request.GET.get("user")
        base_url=f"https://api.modash.io/v1/instagram/profile/{user_handler}/report"
        response = requests.get(base_url, headers=headers)
        return Response({"success":json.loads(response.text)},status=status.HTTP_200_OK)
        
        
    
        
        
