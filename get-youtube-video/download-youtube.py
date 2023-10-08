import pytube
video_url=input('Enter URL: ')

video_instance=pytube.YouTube(video_url)
stream=video_instance.streams.get_highest_resolution()

#download
stream.download()