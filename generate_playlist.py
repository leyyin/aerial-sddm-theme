#!/usr/bin/env python3
import config


videos = config.get_nigh_and_day_videos()
with open("playlist_day.m3u", "w") as file_day:
    for url in videos["day"]:
        print("[+] day - " + url)
        file_day.write(url + "\n")

with open("playlist_night.m3u", "w") as file_night:
    for url in videos["night"]:
        print("[+] night - " + url)
        file_night.write(url + "\n")

