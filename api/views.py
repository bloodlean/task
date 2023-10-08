from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import *
from .permissions import *

from app.models import *
from .serializers import *

@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def user(request):

    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(User, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UserSerializer(User, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)     

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def user_detail(request, pk):

    user = User.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)   

    elif request.method == 'PUT':
        serializer = UserSerializer(User, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    
#TEACHER
@api_view(['GET', 'POST'])
@permission_classes([ProjectPermission])
def project(request):

    if request.method == 'GET':
        project = Project.objects.all()
        serializer = ProjectSerializer(Project, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProjectSerializer(Project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([ProjectDetailPermission])
def project_detail(request, pk):

    project = Project.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=HTTP_202_ACCEPTED) 
    elif request.method == 'PUT':
        serializer = ProjectSerializer(Project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=HTTP_204_NO_CONTENT)

#STUDENTS
@api_view(['GET', 'POST'])
@permission_classes([TaskPermission])
def task(request):

    if request.method == 'GET':
        task = Task.objects.all()
        serializer = TaskSerializer(Task, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializer(Task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([TaskDetailPermission])
def task_detail(request, pk):

    task = Task.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)  
    elif request.method == 'PUT':
        serializer = TaskSerializer(Task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=HTTP_204_NO_CONTENT)