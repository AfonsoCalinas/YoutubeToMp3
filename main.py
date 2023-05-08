import os
from pytube import YouTube

SAVE_PATH = input("Enter the directory you wish to save music in!\n> ")

link = input("Now insert the youtube link!\n> ")

yt = YouTube(link)

print("\nChecking the Video's Streams...")

streams = yt.streams.filter(type='audio', mime_type='audio/mp4')

print("\nI found", len(streams), "audio streams for your video :D\nNow downloading the best one!\n")

audio = streams.last()

audio.download(output_path=SAVE_PATH, filename=yt.title + ".mp3")