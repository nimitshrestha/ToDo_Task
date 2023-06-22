from django.shortcuts import render, HttpResponse
from .models import Task
from rest_framework import permissions, authentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from .serializers import TodoItemSerializer

# Create your views here:
def home(request):
    context = {'success': False}
    if request.method == "POST":
        #Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        date = request.POST['date']
        tag = request.POST['tag']
        stats = request.POST['status']

        #create instance of model
        ins = Task(task_title= title, task_description= desc, due_date= date, tags= tag, status= stats)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)


#show all tasks on webpage
def tasks(request):
    allTask = Task.objects.all()
    context = {'tasks': allTask}
    return render(request, 'tasks.html', context)


#Initialise APIs for CRUD operations
#Get all task
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
class ListToDo(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoItemSerializer


#Get detail of Task
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoItemSerializer


#Create New Task
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
class CreateToDo(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoItemSerializer


#Update an Existing Task
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
class UpdateToDo(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoItemSerializer


#Delete a Task
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])
class DeleteToDo(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TodoItemSerializer