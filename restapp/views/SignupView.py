from restapp.serializers import *
from restapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



#REGISTER USER API
class Register(APIView):
        def post(self,request):
            serializer=Influencer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        
                return Response({"Success": "USER CREATED"},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
           
class UpdateInfluencer(APIView):
    def put(self,request,pk):
        try:
            influencer = User.objects.get(pk = pk)
            print(influencer)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=UserSerializer(influencer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




    