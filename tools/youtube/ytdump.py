# python youtube video Download Quiality : 720p, 480p, 360p, 240p

# import libraries
import pytube
import os
from pytube import YouTube
from tqdm import tqdm


# download video    
def download_video(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download()
    print(f"Downloaded {yt.title} successfully!")

# download playlist
def download_playlist(url):
    playlist = pytube.Playlist(url)
    for video in tqdm(playlist.videos):
        download_video(video.watch_url)

# main function
def main():
    url = input("Enter the URL of the YouTube video or playlist: ")
    if "playlist" in url:
        download_playlist(url)
    else:
        download_video(url)
    print("Download complete!") 