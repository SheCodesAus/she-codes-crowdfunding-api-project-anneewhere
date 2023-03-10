#make sure to use americanized english! 

#serializers help data in the raw form and help convert it into a readable form for the computer to understand

from rest_framework import serializers

from .models import Project, Pledge
from users.serializers import CustomUserSerializer

#this is a manual way to create a serialiser for Project Models. We can create like a automated way to create serializers for each model created
class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() #we don't want the users to change the ID as this is in database. the model already has an ID by default and we are letting the serializer identify the model based of the ID. 
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField() #we don't add auto_now_add as the serializer only talks to the model 
    owner = serializers.ReadOnlyField(source='owner_id')
    total = serializers.ReadOnlyField()

    def create(self,validated_data): #the above links the serializer and model. but we haven't told it what to do.
        return Project.objects.create(**validated_data) #validated_data is a dictionary. ** means creates the values in pairs e.g. key=value. links value to key. (owner=ben)

    def update(self, instance, validated_data): #instance refers to that specific thing
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
        
class PledgeSerializer(serializers.ModelSerializer): #automated version of linking model and serializer
    class Meta: #defines how the model form works.
        model = Pledge
        # fields = '__all__'
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']

supporter = serializers.SerializerMethodField()
def get_supporter(self,object):
    if object.anonymous:
        return "anonymous"
    else:
        return object.supporter.username

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)