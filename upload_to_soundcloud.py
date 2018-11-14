import argparse
import subprocess

def execute_command(command):
  """execute_command - executes the input command in a shell
  Params:
    command (str) - shell command to execute
  Returns:
    stdout (str) - standard output of the shell command
    stderr (str) - standard error of the shell command
  """
  process = subprocess.Popen(command,
                             shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  return stdout, stderr


class Soundcloud():
  
    def __init__(self, filename, title, year):
        self.filename = filename
        self.title = title
        self.year = year
        self.artist = "Robohub Podcast"
        self.album ="Robohub - Connecting the robotics community to the world"
        self.artwork = "robohub_podcast_logo.jpg"

    def create_upload_command(self):
        """create_upload_command - creates the shell command to upload audio to
        soundcloud.

        Returns:
            command (str) - command to 
        """

        options = ['--genre "Technology" --public --downloadable ',
                   '--artist "{}" --album "{}" '.format(self.artist, self.album),
                   '--artwork "{}" --year "{}" '.format(self.artwork, self.year),
                   '--title "{}"'.format(self.title)]

        command = 'sc upload "{}" '.format(self.filename)

        for option in options:
            command += option

        return command

    def upload_to_soundcloud(self):
        upload_command = self.create_upload_command()
        stdout, stderr = execute_command(upload_command)

