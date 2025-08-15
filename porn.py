import phub

# Initialise a client
client = phub.Client()

# Fetch and download a video
video = client.get("https://www.pornhub.com/view_video.php?viewkey=686ea33bc5ffe")
print(video.views)
print(video.date)
print(video.title)
print(video.author.info)
print(f"https://www.pornhub.com/{video.author.url}")
print(video.id)
print(video.duration)
# video = client.get("https://www.pornhub.com/model/mollyredwolf")
# print(video.url)

client = phub.Client()

# Fetch and download a video
video = client.get("https://www.pornhub.com/view_video.php?viewkey=687d0a8fa3e7a")
print(video.views)
print(video.date)
print(video.title)
print(video.author)
print(video.embed)
print(f"https://www.pornhub.com/{video.author.url}")
print(video.id)
print(video.url)
