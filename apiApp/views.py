from django.shortcuts import render
from rest_framework import viewsets ,status
from rest_framework.response import Response
from .models import Movie, Rating
from .serializer import MovieSerializer, RatingSeralizer,UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)

    @action(detail=True,methods=['POST'])
    def rate_movies(self,request,pk=None):
        if 'stars' in request.data:
            movie=Movie.objects.get(id=pk)
            user=User.objects.get(id=1)
            print('movie tirle',movie.name + ' ' + user.username)
            response={'message':'its working'}
            return Response(response,status=status.HTTP_200_OK)
        else:
            response = {'message': 'its not working'}
            return Response(response, status=status.HTTP_204_NO_CONTENT)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSeralizer
    authentication_classes = (TokenAuthentication,)