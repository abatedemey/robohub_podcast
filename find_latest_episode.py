import os
import zipfile

class ZipFiles():

  def __init__(self):
    self.prefix = "episode_"
    self.extension = ".mp3.zip"
    self.unformatted_episode_dir = "episodes/unformatted"

    files_in_dir = os.listdir(self.unformatted_episode_dir)

    self.zip_files = [f for f in files_in_dir if ".zip" in f]


  def is_zip_named_correctly(self, zip_file):
    """is_zip_named_correctly - Checks if all zip files are named in the
    correct format. Raises an error if named incorrectly.
  
    Expected naming format:
      "episode_<episode number>.mp3.zip" 
      i.e. episode_272.mp3.zip
    """
    if len(zip_file) <= len(self.prefix) + len(self.extension):
      print "Filename too short: ", zip_file
      return False

    file_prefix = zip_file[:len(self.prefix)]
    if not file_prefix == self.prefix:
      print "prefix incorrect: '{}' != '{}'".format(file_prefix, self.prefix)
      return False

    file_extension = zip_file[-1*len(self.extension):]
    if not file_extension == self.extension:
      print "extension incorrect: '{}' != '{}'".format(file_extension,
                                                       self.extension)
      return False

    file_episode_number = self.get_episode_number(zip_file)
    if not file_episode_number.isdigit():
      print "episode number incorrect: '{}'".format(file_episode_number)
      return False

    return True

  def get_episode_number(self, zip_file):
    return zip_file.strip(self.prefix).strip(self.extension)

  def get_latest_episode(self):
    episode_numbers = []
    for zip_file in self.zip_files:
      if self.is_zip_named_correctly(zip_file):
        episode_numbers.append(self.get_episode_number(zip_file))
      else :
        # Files in the directory are incorrectly formatted
        # TODO: raise custom exception
        pass

    latest_episode = self.prefix + str(max(episode_numbers)) + self.extension
    return latest_episode

  def unzip_file(self, zip_file):
    path_to_file = os.path.join(self.unformatted_episode_dir, zip_file)
    with zipfile.ZipFile(path_to_file, "r") as zip_ref:
      zip_ref.extractall(self.unformatted_episode_dir)

  def prepare_latest_episode(self):
    latest_episode = self.get_latest_episode()
    self.unzip_file(latest_episode)

if __name__ == "__main__":
  zip_files = ZipFiles()
  zip_files.prepare_latest_episode()

