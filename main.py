from functions import Video
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip


#----------------------------------------------------------
#                   MAIN DRIVER PROGRAM
#   Pick type of video, pick assests, generate video
#
#----------------------------------------------------------

link = "https://youtu.be/R0b-VFV8SJ8?si=cyGGY7xjDvNugDZs"
ttsFile = "sources/test.txt"
outputFile = "output/final.mp4"

vid = Video.combinedProcessing(outputFile, link, ttsFile)