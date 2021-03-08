import eyed3
import sys
from datetime import datetime
import os


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

      self.audiofile = eyed3.load(self.path_to_unformatted_episode)

    def set_id3_tags(self):
      # Initialize tags
      self.audiofile.initTag()

      # Set tags
      self.audiofile.tag.artist = u"Robohub Podcast"
      self.audiofile.tag.album = u"Robohub - Connecting the robotics community to the world"
      self.audiofile.tag.title = unicode(self.title, "utf-8")
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
    print "Please enter all input arguments. i.e.\n\t\
           python prepare_id3_tags.py <audio filename> \
           <episode title> <episode number> <release date 'YYYYMMDD'>"
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
    print "File does not exist"
    sys.exit()

  # Edit episode id3 tags and rename the file
  episode_audio_file.prepare_for_publishing()
