from django.shortcuts import render, redirect, get_object_or_404
from .forms import SongForm
from googletrans import Translator
from .models import Vocabulary,Song
import requests

def index(request): # function for main page
    url = 'https://api.lyrics.ovh/v1/{}/{}' # api url

    if request.method == 'POST' and 'lyrics' in requests.get(url.format(request.POST['artist'], request.POST['title'])).json(): # check request method and have we artist with this song title
        temp = Song.objects.filter(artist = request.POST['artist'],title=request.POST['title']) # if artist with title exist on our database get this object
        if temp: # if we have already have object with same title and artist
            temp.delete() # delete this object for avoid copy on our database
        form = SongForm(request.POST) # creating object with form
        form.save() # save object

    form = SongForm() # empty form for context

    all_my_song = [] # for store all information about song from database

    for s in Song.objects.all().order_by('-id')[:5]: # loop for last 5 song object from database of Song
        song_info = { # dictionary for storing information on song object
            'title': s.title,
            'artist': s.artist,
            'id': s.id
        }
        all_my_song.append(song_info) # adding info about current song


    context = {'form': form,'all_my_song':all_my_song} # context dictionary for get information by keys on html page

    return render(request,'lern_by/index.html',context)

def add_vocabulary(request,word,id): # function for adding word to Vocabulary
    temp = Vocabulary.objects.filter(word=word) # if word exist on our database get this object
    if temp: # if already have one
        temp.delete() # then delete this object for avoid copy on our database
    tr_word = Translator().translate(word,dest='ru').text # translate word to Russian language
    Vocabulary.objects.create(word=word,translated_word=tr_word) # create object
    return redirect('/song/' + str(id)) # return to our song


def vocabulary(request): # function for returning all information on Vocabulary
    vocabulary = [] # where we will have all info
    for v in Vocabulary.objects.all().order_by('-id'):# loop for getting all object on reversing order(from newest to oldest)
        d = { # dictionary for storing information on Vocabulary object
            'word': v.word,
            'translated_word': v.translated_word,
            'id': v.id
        }
        vocabulary.append(d) # adding info about current word
    context = {'vocabulary':vocabulary} # context dictionary for get information by keys on html page
    return render(request,'lern_by/vocabulary.html',context) # return to vocabulary page

def song(request,pk):# function for returning information about Song
    s = Song.objects.get(pk=pk) # get object from database by primary key
    url = 'https://api.lyrics.ovh/v1/{}/{}' # url api
    res = requests.get(url.format(s.artist, s.title)).json() # get dictionary info from api
    lyrics = res['lyrics'].splitlines() # get lyrics info
    for i in range(len(lyrics)):
        lyrics[i] = lyrics[i].split() # split song string to line

    song_info = { # dictionary for get information by keys on html page
        'title': s.title,
        'artist': s.artist,
        'lyrics': lyrics,
        'id': s.id
    }

    return render(request,'lern_by/song.html',song_info) # return to song page

def song_delete(request,pk): # function for deleting object form database Song
    song = get_object_or_404(Song,pk=pk) # get object by primary key

    if request.method == 'POST': # check method
        song.delete() # delete object
        return redirect('/')

    return render(request,'lern_by/index.html',{'city': song})

def song_delete_all(request): # function for deleting all object form database Song
    song = Song.objects.all() # get all objects from database Song
    song.delete() # delete all objects
    return redirect('/')


def word_delete(request,pk):# function for deleting object form database Vocabulary
    word = get_object_or_404(Vocabulary,pk=pk) # get object by primary key

    if request.method == 'POST': # check method
        word.delete()# delete object
        return redirect('/vocabulary')

    return redirect('/vocabulary')

def word_delete_all(request):# function for deleting all object form database Vocabulary
    word = Vocabulary.objects.all() # get all objects from database Vocabulary
    word.delete() # delete all objects
    return redirect('/vocabulary')

def word_move_to_top(request,pk):
    word = Vocabulary.objects.get(pk = pk)  # get object by primary key
    w,t = word.word,word.translated_word # store template value

    word.delete() # delete object

    Vocabulary.objects.create(word=w,translated_word=t) # create new object
    return redirect('/vocabulary')


