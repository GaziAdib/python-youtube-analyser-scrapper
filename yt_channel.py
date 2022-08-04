from pytube import Channel

channel_link = input('Enter Channel Link: ')

channel = Channel(channel_link)

## channel name
print(channel.channel_name)

## channel url

print(channel.channel_url)

## lenth of videos in my channel

print(len(channel.video_urls))

## download all the channel videos

for video in channel.videos:
    video.streams.get_highest_resolution().download()

## download last 3 video from a channel

for video in channel.videos[:3]:
    video.streams.get_highest_resolution().download()


## get last 10 video urls from a channel
for video in channel.video_urls[:10]:
    print(video)



