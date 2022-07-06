#!/bin/bash
set -e

FILE=$1
EPISODE_TITLE=$2
EPISODE_NUMBER=$3
RELEASE_DATE=$4

SOUNDCLOUD_RSS_FEED=$(cat config/soundcloud_rss_feed)

# Exit script if input is not given
if [ -z $4 ]
then
  echo "This script find the latest episodes in episodes/unformatted directory"
  echo "then prepares the ID3 tags for publishing to soundcloud."
  echo
  echo "Enter all input arguments"
  echo "i.e. ./publish_episode.sh <filename> <episode_title> <episode_number> <release_date>"
  echo "./publish_episode.sh episode_271.mp3 'A Whimsical Robotic Artist' 271 20181012"
  exit 0
fi

#python src/find_latest_episode.py
python3 src/prepare_id3_tags.py "$FILE" "$EPISODE_TITLE" "$EPISODE_NUMBER" "$RELEASE_DATE"
