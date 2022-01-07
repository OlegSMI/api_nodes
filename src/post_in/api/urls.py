from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
urlpatterns = router.urls


#для NoteViewSet

# notes_list = NoteViewSet.as_view({
#     'get': 'list',
#     'post': 'crrate'
# })
    
# notes_detail = NoteViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })


#для всех остальных

# urlpatterns =[
#     # path('notes/', NoteListView.as_view()),
#     # path('notes/<int:pk>', NoteDetailView.as_view(), name='notes_detail')
#     path('notes/', notes_list, name='notes_list'),
#     path('notes/<int:pk>', notes_detail, name='notes_detail')
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)