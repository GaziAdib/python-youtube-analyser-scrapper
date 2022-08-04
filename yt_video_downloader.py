import pytube
from pytube import exceptions

# input from user -- video url

url = input('Enter a video URL:')

# parse it

try:
    yt = pytube.YouTube(url)
except exceptions.VideoPrivate:
    print('Video is Private') 
except exceptions.VideoRegionBlocked:
    print('Video is blocked')
except exceptions.VideoUnavailable:
    print('Video is Unavailable')       
else:
    yt.streams.get_highest_resolution().download()
    print('Video Downloaded...')
