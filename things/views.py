from django.shortcuts import render
from rest_framework import generics
from .models import Thing,Post
from .serializers import ThingSerializers ,PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly
# Create your views here.
class ThingList(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializers
    permission_classes = [IsAuthenticated]

class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializers
    permission_classes = [IsOwnerOrReadOnly]

class PostsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    

# RetrieveAPIView RetrieveUpdateAPIView
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
   