from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Comment,Category,Movie
from .serializers import CommentSerializer,MovieSerializer


class MovieApiView():
    def get(self, request: Request,pk=None):
        if pk:
            try:
                movie=Movie.objects.get(id=pk)
                return Response(MovieSerializer(movie).data)
            except:
                return Response({"message":"does not exists"})
        movie= Movie.objects.all()
        return Response(MovieSerializer(movie, many=True).data)


    def post(self, request: Request,pk=None):
        if not pk:
            serializer = MovieSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            movie= serializer.save()
        return Response(MovieSerializer(movie).data)


    def put(self, request: Request, pk=None):
        if pk:
            try:
                movie= Movie.objects.get(pk=pk)
                serializer = MovieSerializer(instance=movie, data=request.data)
                serializer.is_valid(raise_exception=True)
                movie = serializer.save()
                return Response(MovieSerializer(movie).data)
            except:
                return Response({"message": "does not exists"})
        return Response({"message":"Method Put not allowed"})


    def delete(self,request:Request,pk=None):
        if pk:
            movie=Movie.get(id=pk)
            movie.delete()
            return Response({"message":"succes"})
        else:
            return Response({"message":"Method Delete not allowed"})



class CommentApiView():
    def get(self, request: Request,pk=None):
        if pk:
            try:
                comment=Comment.objects.get(id=pk)
                return Response(CommentSerializer(comment).data)
            except:
                return Response({"message":"does not exists"})
        comment= Comment.objects.all()
        return Response(CommentSerializer(comment, many=True).data)


    def post(self, request: Request,pk=None):
        if not pk:
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            comment= serializer.save()
        return Response(CommentSerializer(comment).data)


    def put(self, request: Request, pk=None):
        if pk:
            try:
                comment= Comment.objects.get(pk=pk)
                serializer = CommentSerializer(instance=comment, data=request.data)
                serializer.is_valid(raise_exception=True)
                comment = serializer.save()
                return Response(CommentSerializer(comment).data)
            except:
                return Response({"message": "does not exists"})
        return Response({"message":"Method Put not allowed"})


    def delete(self,request:Request,pk=None):
        if pk:
            comment=Comment.get(id=pk)
            comment.delete()
            return Response({"message":"succes"})
        else:
            return Response({"message":"Method Delete not allowed"})