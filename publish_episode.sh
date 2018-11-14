#!/bin/bash
set -e

FILE=$1
EPISODE_TITLE=$2
EPISODE_NUMBER=$3
RELEASE_DATE=$4

# Exit script if input is not given
if [ -z $4 ]
then
  echo "Enter all input arguments"
  echo "i.e. ./publish_episode.sh <filename> <episode_title> <episode_number> <release_date>"
  echo "./publish_episode.sh episode_271.mp3 'A Whimsical Robotic Artist' 271 20181012"
  exit 0
fi


python prepare_id3_tags.py "$FILE" "$EPISODE_TITLE" "$EPISODE_NUMBER" "$RELEASE_DATE"
#./upload_to_soundcloud.sh $FILE $EPISODE_TITLE

echo "Manually edit the soundcloud upload to enable downloads and include in RSS feed"
