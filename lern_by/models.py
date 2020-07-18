from django.db import models

class Song(models.Model): # create database
    artist = models.CharField(max_length=30) # column with name (artist) and input info CharField with maximum length equal to 30 char
    title = models.CharField(max_length=30) # column with name (title) and input info CharField with maximum length equal to 30 char

    def __str__(self):
        return self.title


class Vocabulary(models.Model):
    word = models.CharField(max_length=30) # column with name (word) and input info CharField with maximum length equal to 30 char
    translated_word = models.CharField(max_length=30)  # column with name (translated_word) and input info CharField with maximum length equal to 30 char

    def __str__(self):
        return self.word
