from django.urls import path
from . import views

urlpatterns = [
    path('',views.index), # calling function from views.py for main page
    path('song/<int:id>/<str:word>', views.add_vocabulary),# calling function from views.py for adding word to vocabulary
    path('vocabulary',views.vocabulary), # calling function from views.py for vocabulary page
    path('vocabulary/delete/<int:pk>',views.word_delete), # calling function from views.py for deleting word from database of vocabulary
    path('vocabulary/delete_all',views.word_delete_all), # calling function from views.py for deleting all word from database of vocabulary
    path('vocabulary/move_to_top/<int:pk>', views.word_move_to_top), # calling function from views.py for deleting word and adding word to head of vocabulary
    path('song/<int:pk>',views.song),# calling function from views.py  for song page
    path('delete/<int:pk>',views.song_delete), # calling function from views.py for deleting song from database of Song
    path('delete_all',views.song_delete_all) # calling function from views.py for deleting all song from database of Song
]