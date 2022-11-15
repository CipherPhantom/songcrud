from django.shortcuts import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from musicapp.models import Artiste, Song, Lyric

from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer

# Create your views here.
def index(request):
    return HttpResponse("<h1'>Welcome to The Music App Api</h1>")


# Artiste api
@api_view(['GET', 'POST'])
def artiste_list_api(request):
    if request.method == "GET":
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artiste_detail_api(request, id):
    try:
        artiste = Artiste.objects.get(id=id)
    except Artiste.DoesNotExist:
        return Response({"message": f"Artiste with id {id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer =  ArtisteSerializer(artiste)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method  == "PUT":
        serializer = ArtisteSerializer(artiste, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        artiste.delete()
        return Response({"message": "Artiste successfully deleted."}, status=status.HTTP_204_NO_CONTENT)


# Song api
@api_view(['GET', 'POST'])
def song_list_api(request):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def song_detail_api(request, id):
    try:
        song = Song.objects.get(id=id)
    except Song.DoesNotExist:
        return Response({"message": f"Song with id {id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer =  SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method  == "PUT":
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        song.delete()
        return Response({"message": "Song successfully deleted."}, status=status.HTTP_204_NO_CONTENT)


# Lyric api
@api_view(['GET', 'POST'])
def lyric_list_api(request):
    if request.method == "GET":
        lyrics = Lyric.objects.all()
        serializer = LyricSerializer(lyrics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = LyricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def lyric_detail_api(request, id):
    try:
        lyric = Lyric.objects.get(id=id)
    except Lyric.DoesNotExist:
        return Response({"message": f"Lyric with id {id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer =  LyricSerializer(lyric)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method  == "PUT":
        serializer = LyricSerializer(lyric, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        lyric.delete()
        return Response({"message": "Lyric successfully deleted."}, status=status.HTTP_204_NO_CONTENT)


