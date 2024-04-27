from functions import downloadVideo, createTTS, edit
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from datetime import timedelta

#----------------------------------------------------------
#                   MAIN DRIVER PROGRAM
#   Pick type of video, pick assests, generate video
#
#----------------------------------------------------------

link = "https://www.youtube.com/watch?v=952ILTHDgC4"
ttsFile = "test.txt"
res = downloadVideo(link, "test.mp4")
createTTS(ttsFile, "test.mp3")
edit("test.mp3", "test.mp4", res, "testOutput.mp4")