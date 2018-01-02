#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -ne 1 ]]; then
    echo "Run with: "
    echo "$0 <PLAYLIST_VIDEOS_DIR>"
    exit 1
fi


function check_directory()
{
    if [[ ! -d $1 ]]; then
        echo "Error: '$1' is not a directory/does not exist."
        echo -e "Run download_playlist_offline.py first OR make a directory with the following structure:"
        echo -e "
    <PLAYLIST_VIDEOS_DIR>:
        <PLAYLIST_VIDEOS_DAY_DIR>:
            day_file_1.mov
            day_file_2.mov
            ...

        <PLAYLIST_VIDEOS_NIGHT_DIR>:
            night_file_1.mov
            night_file_2.mov
            ...
        "
        exit 1
    fi
}

DIR_PLAYLIST=$(readlink -f "$1")
DIR_PLAYLIST_DAY="$DIR_PLAYLIST/day"
DIR_PLAYLIST_NIGHT="$DIR_PLAYLIST/night"

check_directory "$DIR_PLAYLIST"
check_directory "$DIR_PLAYLIST_DAY"
check_directory "$DIR_PLAYLIST_NIGHT"

# Generate playlist files
echo "Generating playlist file playlist_day_offline.m3u"
find "$DIR_PLAYLIST_DAY" -maxdepth 1 -type f > playlist_day_offline.m3u

echo "Generating playlist file playlist_night_offline.m3u"
find "$DIR_PLAYLIST_NIGHT" -maxdepth 1 -type f > playlist_night_offline.m3u
