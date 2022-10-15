#importing the youtube
from pytube import YouTube

#Initialization
yt = YouTube('https://www.youtube.com/watch?v=-KnAZcXzxRA')

#Gets the first stream
stream = yt.streams.first()

#Downloading
stream.download()
