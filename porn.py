import phub

# Initialise a client
client = phub.Client()

# Fetch and download a video
video = client.get("https://www.pornhub.com/view_video.php?viewkey=686ea33bc5ffe")
print(video.views)
video = client.get("https://www.pornhub.com/model/mollyredwolf")
print(video.views)
