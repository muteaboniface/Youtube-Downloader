from pytube import YouTube
from datetime import datetime

YT_LINK = input('Paste the youtube download link here: \n    > ')
video = YouTube(YT_LINK)

#Showing details
print("\n\nTitle: ",video.title)
print("Number of views: ",video.views)
MIN = int(video.length / 60)
SEC = video.length % 60
print(f"Length of video: {MIN}min:{SEC}sec")
print(f"Rating of video: {video.rating}\n\n")



# getting the highest resolution
data = video.streams.get_highest_resolution()

#save video
DESTINATION_FOLDER = 'D:\Entertainment\YT'
print("Downloading...")
now = datetime.now()

# Elapsed Time

data.download(DESTINATION_FOLDER,timeout=60,max_retries=1)
end = datetime.now()
print("Download completed!!")
print(f'Elapsed time: {end-now}')