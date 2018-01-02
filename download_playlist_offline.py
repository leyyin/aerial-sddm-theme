#!/usr/bin/env python3
import config
import os

import subprocess


DIR_VIDEOS = os.path.join(os.getcwd(), 'playlist_videos')
DIR_VIDEOS_DAY = os.path.join(DIR_VIDEOS, 'day')
DIR_VIDEOS_NIGHT = os.path.join(DIR_VIDEOS, 'night')


def download_to_file(url_from, file_destination):
    print("Downloading {} to {}".format(url_from, file_destination))
    # Use wget as it has nicer features and easier to use
    subprocess.check_output(['wget', '--continue', '-O', file_destination, url_from])
    # import urllib.request
    # import shutil
    # with urllib.request.urlopen(url_from) as response, open(file_destination, 'wb') as out_file:
    #     shutil.copyfileobj(response, out_file)


# Create playlist directories if it does not exist
if not os.path.exists(DIR_VIDEOS_DAY):
    print("Creating {}".format(DIR_VIDEOS_DAY))
    os.makedirs(DIR_VIDEOS_DAY)
if not os.path.exists(DIR_VIDEOS_NIGHT):
    print("Creating {}".format(DIR_VIDEOS_NIGHT))
    os.makedirs(DIR_VIDEOS_NIGHT)


print("\nDownloading day videos")
videos = config.get_nigh_and_day_videos()
for url in videos["day"]:
    filename = os.path.basename(url)
    download_to_file(url, os.path.join(DIR_VIDEOS_DAY, filename))

print("\nDownloading night videos")
for url in videos["night"]:
    filename = os.path.basename(url)
    download_to_file(url, os.path.join(DIR_VIDEOS_NIGHT, filename))
