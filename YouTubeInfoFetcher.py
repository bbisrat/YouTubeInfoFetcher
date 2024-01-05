from pytube import YouTube

# Prompt the user to enter the YouTube video URL
link = input("Please input link of Youtube video: ")

# Create a YouTube object using the provided link
ytt = YouTube(link)

# Print the title and view count of the video
print("Title:", ytt.title)
print("Views:", ytt.views)
