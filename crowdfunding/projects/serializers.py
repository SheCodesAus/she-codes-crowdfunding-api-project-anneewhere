#make sure to use americanized english! 

#serializers help data in the raw form and help convert it into a readable form for the computer to understand

from rest_framework import serializers

from .models import Project, Pledge

#this is a manual way to create a serialiser for Project Models. We can create like a automated way to create serializers for each model created
class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() #we don't want the users to change the ID as this is in database. the model already has an ID by default and we are letting the serializer identify the model based of the ID. 
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField() #we don't add auto_now_add as the serializer only talks to the model 
    owner = serializers.CharField(max_length=200)

    def create(self,validated_data): #the above links the serializer and model. but we haven't told it what to do.
        return Project.objects.create(**validated_data) #validated_data is a dictionary. ** means creates the values in pairs e.g. key=value. links value to key. (owner=ben)

class PledgeSerializer(serializers.ModelSerializer): #automated version of linking model and serializer
    class Meta: #defines how the model form works.
        model = Pledge
        fields = '__all__'
        # fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter'] - is the manual way to do the above
        