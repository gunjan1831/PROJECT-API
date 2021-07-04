from movielist_app.models import WatchList,StreamPlatform , Review
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from movielist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404




class ReviewCreate(generics.CreateAPIView):  #review for a particular movie.
    serializer_class = ReviewSerializer

    def perform_create(self):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)


        serializer.save(watchlist=watchlist)


class ReviewList(generics.ListCreateAPIView):
   serializer_class = ReviewSerializer


   def get_queryset(self):
       pk = self.kwargs['pk']
       return Review.objects.filter(watchlist=pk)






class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer






# class ReviewDetails(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self,request, *args,**kwargs):
#         return self.retrieve(request, *args,**kwargs)
#
#
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self,request, *args,**kwargs):
#         return self.list(request, *args,**kwargs)
#
#     def post(self,request, *args,**kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# class StreamPlatformVS(viewsets.ViewSet):
#
#     def list(self , request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many= True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)
#
#     def create(self,request):
#         serializer =StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class StreamPlatformAV(APIView):

    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializer =StreamPlatformSerializer(platform,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors)

class StreamPlatformDetailsAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class WatchListAV(APIView):

    def get(self,request):
         movies = WatchList.objects.all()
         serializer = WatchListSerializer(movies, many=True)
         return Response(serializer.data)

    def post(self, request):
           serializer = WatchListSerializer(data=request.data)
           if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
           else:
                 return Response(serializer.errors)


class WatchDetailsAV(APIView):

    def get(self,request,pk):
        try:
             movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
             return Response({'Error':'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self,request,pk):
            movie = WatchList.objects.get(pk=pk)
            serializer  = WatchListSerializer(movie, data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            else:
               return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#
# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#
#     if request.method == 'GET':
#         try:
#              movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer  = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#         else:
#            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#


