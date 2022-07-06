import eyed3
import sys
import os


def episode_prep_success():
    msg = [
        "Episode has been prepared. Follow the instructions below to complete publishing: ",
        "Step 1. Uploading the episode to soundcloud",
        "      a.  Go to soundcloud.com and upload the formatted episode.",
        "      b.  Select 'Enable Downloads', 'Include in RSS feed'",
        "      c.  Select the 'Genre' as 'Technology'\n\n",
        "Step 2. Getting the embedded soundcloud link",
        "      a.  Once the episode has finished processing on Soundcloud, press the 'share' button",
        "      b.  In the Screen that pops up, press 'embed' then select the option with the ",
        "          logo and audio graph side by side with each other.",
        "      c.  Copy the code form the 'Code and Preview' box",
        "      d.  Go to the WordPress post for this episode",
        "      e.  Add the embedded soundcloud link immediately after the first image.\n\n",
        "Step 3. Getting the mp3 download link from the RSS feed.",
        "      a.  Go to the soundcloud RSS soundfeed:",
        "          $SOUNDCLOUD_RSS_FEED",
        "      b.  Copy the latest audio mp3 link listed in the following format:",
        '      c.  <enclosure type="audio/mpeg" url="<COPY THIS LINK>" length="<LENGTH OF LINK>"/>',
        "      d.  Go to the WordPress post for this episode",
        "      e.  Update the 'Download mp3' link with the mp3 download link",
        "      f.  Add the 'aa_mp3_link' custom field with the mp3 download link"]
    print("\n".join(msg))


class EpisodeAudioFile():

    def __init__(self, filename, title, episode_num, release_date):
        self.filename = filename
        self.title = title
        self.episode_num = episode_num
        self.release_date = release_date
        self.year = release_date[0:4]
        self.cover_art_path = "assets/robohub_podcast_logo.jpg"
        self.path_to_all_formatted_episodes = "episodes/ready_to_publish"
        self.path_to_unformatted_episode = os.path.join("episodes/unformatted", filename)
        print("year = ", self.year)
        print("path_to_unformatted_episode = ", self.path_to_unformatted_episode)

        self.audiofile = eyed3.load(self.path_to_unformatted_episode)

    def get_duration(self):
        duration_secs = self.audiofile.info.time_secs
        return duration_secs / 60.0

    def set_id3_tags(self):
        print()
        # Initialize tags
        self.audiofile.initTag()

        # Set tags
        self.audiofile.tag.artist = u"Robohub Podcast"
        self.audiofile.tag.album = u"Robohub - Connecting the robotics community to the world"
        self.audiofile.tag.title = self.title
        print("audio tag: ")
        print(self.audiofile.tag.title)
        print("audio tag done ")

        self.audiofile.tag.track_num  = int(self.episode_num)
        self.audiofile.tag.composer = u"Produced by Robohub"
        self.audiofile.tag.release_date = self.year
        self.audiofile.tag.recording_date = self.year


    def set_cover_image(self):
      cover_art = open(self.cover_art_path, "rb").read()
      self.audiofile.tag.images.set(3, cover_art, "image/jpeg")

    def save_id3_changes(self):
      self.audiofile.tag.save()

    def rename_file(self):
      output_filename = "robots-{}-episode{}.mp3".format(release_date,
                                                         episode_num)
      path_to_formatted_episode = os.path.join(self.path_to_all_formatted_episodes,
                                               output_filename)

      os.rename(self.path_to_unformatted_episode, path_to_formatted_episode)

    def prepare_for_publishing(self):
      self.set_id3_tags()
      self.set_cover_image()
      self.save_id3_changes()
      self.rename_file()

if __name__ == "__main__":
  if len(sys.argv) != 5:
    msg = "Please enter all input arguments. i.e.\n\t\
           python prepare_id3_tags.py <audio filename> \
           <episode title> <episode number> <release date 'YYYYMMDD'>"
    print(msg)
    sys.exit(1)
  else:
    filename = sys.argv[1]
    title = sys.argv[2]
    episode_num = sys.argv[3]
    release_date = sys.argv[4]


  episode_audio_file = EpisodeAudioFile(filename=filename,
                                        title=title,
                                        episode_num=episode_num,
                                        release_date=release_date)

  # Exit if the file doesnt exist
  if not os.path.exists(episode_audio_file.path_to_unformatted_episode):
    print("File does not exist")
    sys.exit()

  audio_duration_mins = episode_audio_file.get_duration()
  if audio_duration_mins < 7:
      print("Audio too short. Duration = {} mins".format(audio_duration_mins))
      sys.exit()

  # Edit episode id3 tags and rename the file
  episode_audio_file.prepare_for_publishing()
  episode_prep_success()
