# robohub_podcast
Tools to automate production of Robohub Podcast episodes

Usage:
1. Download the desired episode and place it in `episodes/unformatted/<desired_episode>.mp3`

2. run `./publish_episode.sh <filename> <episode_title> <episode_number> <release_date>`

i.e. ./publish_episode.sh episode_271.mp3 'A Whimsical Robotic Artist' 271 20181012

3. The formatted episode will be in `episodes/ready_to_publish/<formatted_episode>.mp3`

