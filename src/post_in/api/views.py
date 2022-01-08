# from django.shortcuts import render
# from django.http import response
from typing import Generic
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from notes.models import Note
from api.serializers import NoteSerializer, ThinNoteSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.mixins import (ListModelMixin, CreateModelMixin, RetrieveModelMixin,
UpdateModelMixin, DestroyModelMixin)
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsAuthorOrReadOnly

class UserViewSet(ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class NoteViewSet(ModelViewSet):
    model = Note
    queryset = model.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthorOrReadOnly,)
   #http_method_names = ['get', 'post' ] #ограничение какие методы используются
    def list(self, request, *args, **kwargs):
        notes = Note.objects.all()#filter(author=request.user.id)# чтобы видел только тот, кто создал
        context = {'request': request}
        serializer = ThinNoteSerializer(notes, many=True, context=context)
        return Response(serializer.data)

# замена функции list с более удобным функционалом
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ThinNoteSerializer
    #     return NoteSerializer

    def get_queryset(self):
        if self.request.user.admin_is:
            return self.model.objects.all()
        return self.model.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#способ четвертый, плохо мной разобран, но короткий

# class NoteListView(ListCreateAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     def list(self, request, *args, **kwargs):
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThinNoteSerializer(notes, many=True, context=context)
#         return Response(serializer.data)

# class NoteDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer



#способ третий, здесь второй класс берется из второго способа

# class NoteListView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     def get(self, request, *args, **kwargs):
#         self.serializer_class = ThinNoteSerializer
#         return self.list(request, *args, **kwargs)

#     def create(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


#способ второй

# class NoteListView(APIView):
#     def get(self, request, format=None):
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThinNoteSerializer(notes, many=True, context=context)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class NoteDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Note.objects.get(pk=pk)
#         except Note.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     def get(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         note = self.get_object(pk)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#самый первый способ

# @api_view(['GET', 'POST']) #отображение целой страницы
# def notes_list(request, format=None):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE']) #отображение частей
# def notes_detail(request, pk, format=None):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
