from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status, generics

#linking the serializer and the model
from .models import Project, Pledge
from. serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer

# Create your views here.
class ProjectList(APIView):

    def get(self, request): #self because it is a class
        projects = Project.objects.all() #collecting all the projects in this class
        serializer = ProjectSerializer(projects, many=True) #serializers need to know that there are many objects.
        return Response(serializer.data)
    
    def post(self,request): #submitting the data. the request is specifically talking about the payload
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #status is imported from the django http stuff
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #we don't have to write a "else" here because once it runs the if statement, and it successfuly runs the response, it won't do the other response. 
    
    #when you run the above post, you can post raw JSON file using the URL. 

class ProjectDetail(APIView): #shows us specific details of the project

    def get_object(self,pk): #this is defined in bottom def
        try:
            return Project.objects.get(pk=pk) #primary key equals the value it was given. if get_object(self,monkey), then on this line it is (pk=monkey)
        except Project.DoesNotExist:
            raise Http404 #when we raise an error, django knows how to handle it.

    def get(self, request, pk): #this is will run
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

class PledgeList(generics.ListCreateAPIView): #lists and creates the view. using 'generic' helps us create a form instead of showing it as a JSON. 
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer