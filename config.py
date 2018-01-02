#!/usr/bin/env python3
import urllib.request
import json

JSON_URL = 'http://a1.phobos.apple.com/us/r1000/000/Features/atv/AutumnResources/videos/entries.json'


def get_json_videos():
    response = urllib.request.urlopen(JSON_URL)
    text = response.read().decode('utf-8')
    return json.loads(text)


def get_nigh_and_day_videos():
    videos = {
        "night": [],
        "day": []
    }

    for json_object in get_json_videos():
        for asset in json_object["assets"]:
            if asset["timeOfDay"] == "night":
                videos["night"].append(asset["url"])
            elif asset["timeOfDay"] == "day":
                videos["day"].append(asset["url"])

            else:
                print("Unknown time of day %s" % asset["timeOfDay"])

    return videos

