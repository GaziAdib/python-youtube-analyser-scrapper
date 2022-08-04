from pytube import Playlist

playlist_url = 'https://www.youtube.com/watch?v=5q3crAMieVU&list=PLPip5lOh2Z5BY936bUdHF8uU0JOK-R5qG'

playlist = Playlist(playlist_url)

# get the lenth of playlist video
print(len(playlist.video_urls))


# Get last 3 video url from playlist

for video in playlist.video_urls[:3]:
    print(video)

# Download Playlist video in High Resolution

for video in playlist.videos[:10]:
    video.streams.get_highest_resolution().download()

print('downloaded')    
