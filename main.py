from functions import downloadVideo, createTTS, createBaseVideo, Video, Audio
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip


#----------------------------------------------------------
#                   MAIN DRIVER PROGRAM
#   Pick type of video, pick assests, generate video
#
#----------------------------------------------------------

link = "https://www.youtube.com/watch?v=952ILTHDgC4"
ttsFile = "sources/test.txt"

# Check if background video is already downloaded or not
try:
    vid = downloadVideo(link, "output/test.mp4")
except FileExistsError:
    print("Vid already existed, so did not re-download")
    vid = Video("output/test.mp4", 720)

# Check if TTS is already created or not
try:
    tts = createTTS(ttsFile, "output/test.mp3")
except FileExistsError:
    print("TTS already existed, so did not re-download")
    tts = Audio(ttsFile)


# Check if Base Video is already created or not
try:
    createBaseVideo(tts.fileName, vid.fileName, "output/testOutput.mp4", vid.res)
except FileExistsError:
    print("Final video already exists, new one NOT CREATED")