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

echo "Episode has been prepared. Follow the instructions below to complete publishing: "
echo "Step 1. Uploading the episode to soundcloud"
echo "      a.  Go to soundcloud.com and upload the formatted episode."
echo "      b.  Select 'Enable Downloads', 'Include in RSS feed'"
echo "      c.  Select the 'Genre' as 'Technology'"
echo
echo
echo "Step 2. Getting the embedded soundcloud link"
echo "      a.  Once the episode has finished processing on Soundcloud, press the 'share' button"
echo "      b.  In the Screen that pops up, press 'embed' then select the option with the "
echo "          logo and audio graph side by side with each other."
echo "      c.  Copy the code form the 'Code and Preview' box"
echo "      d.  Go to the WordPress post for this episode"
echo "      e.  Add the embedded soundcloud link immediately after the first image."
echo
echo
echo "Step 3. Getting the mp3 download link from the RSS feed."
echo "      a.  Go to the soundcloud RSS soundfeed:"
echo "          $SOUNDCLOUD_RSS_FEED"
echo "      b.  Copy the latest audio mp3 link listed in the following format:"
echo '      c.  <enclosure type="audio/mpeg" url="<COPY THIS LINK>" length="<LENGTH OF LINK>"/>'
echo "      d.  Go to the WordPress post for this episode"
echo "      e.  Update the 'Download mp3' link with the mp3 download link"
echo "      f.  Add the 'aa_mp3_link' custom field with the mp3 download link"
echo
echo
