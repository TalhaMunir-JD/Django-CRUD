from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status

#list wise views - detail views-objectwise
# Create your views here.
class Views:
    @api_view(['GET'])
    def getData(request):
        app = Task.objects.all()
        serializer = TaskSerializer(app, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['POST'])
    def postData(request):
        print("request is: ", request)
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        message = 'post request executed beautifully'
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    def putData(request, pk):
        try:
            task = Task.objects.get(pk=pk)
            print(task)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['Delete'])
    def deleteData(request, pk):
        try:
            task = Task.objects.get(pk=pk)
            print(task.pk)
            print(task.name)
        except task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(status=status.HTTP_200_OK)

    @api_view(['GET'])
    def searchData(request):
        app = Task.objects.filter(name__icontains=request.data)
        serizalizer = TaskSerializer(app, many=True)
        return Response(serizalizer.data)