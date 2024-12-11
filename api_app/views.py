from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from expenses.models import Expense,Category
from api_app.serializers import ExpenseSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class get_expenses(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        queryset = Expense.objects.all()
        serializer = ExpenseSerializer(queryset,many=True)
        return Response ({
            "status":True,
            "data":serializer.data
        })

    def post(self,request):
        data = request.data
        serializer = ExpenseSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                "message":"data not saved",
                "errors": serializer.errors,
            })
        serializer.save()
        return Response({
            "message":"data saved",
            "data":serializer.data
        })
    
    def put(self,request):
        data = request.data

        if not data.get('id'):
            return Response({
                "message":"data not saved",
                "errors":"id is required",
            })
        
        expense = Expense.objects.get(id = data.get('id'))
        serializer = ExpenseSerializer(expense,data=data)

        if not serializer.is_valid():
            return Response({
                "message":"data not saved",
                "errors":serializer.errors,
            })
        
        serializer.save()
        
        
        return Response({
            "message":"data saved",
            "data":serializer.data
        })
    
    def patch(self,request):
        data = request.data

        if not data.get('id'):
            return Response({
                "message":"data not saved",
                "errors":"id is required",
            })
        
        expense = Expense.objects.get(id = data.get('id'))
        serializer = ExpenseSerializer(expense,data=data,partial=True)

        if not serializer.is_valid():
            return Response({
                "message":"data not saved",
                "errors":serializer.errors,
            })
        
        serializer.save()
        
        
        return Response({
            "message":"data saved",
            "data":serializer.data
        })

    def delete(self,request):
        data = request.data

        if not data.get('id'):
            return Response({
                "message":"data not updated",
                "errors":"id is required"
            })
        
        expense = Expense.objects.get(id = data.get('id')).delete()

        return Response({
            "message":"data deleted",
            "data" : {}
        })

class LoginAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "stutus":False,
                "data": serializer.errors
            })
        username = serializer.data['username']
        password = serializer.data['password']


        user_obj = authenticate(username = username,password = password)
        if user_obj:
            token , _ = Token.objects.get_or_create(user=user_obj)
            print(token)
            return Response({
                "status":True,
                "data":{'token':''}
            })
        
        return Response({
            "status":True,
            "data":{},
            "message":"Invalid credentials"
        })