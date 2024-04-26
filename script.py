from pytube import YouTube
from moviepy.editor import *
from tiktokvoice import tts
from functions import downloadVideo
# STEP 1: Download the minecraft parkour video
newlink = "https://www.youtube.com/watch?v=952ILTHDgC4"
downloadVideo(newlink)
'''yt = YouTube(newlink)
videoStream = yt.streams.filter(adaptive=True, file_extension="mp4", type="video")
print(videoStream)'''
# videoStream.download(filename="bottom.mp4")
'''
# STEP 2: Do the resolution calculations (used later for cropping)
resolution = videoStream.resolution
if (resolution == "720p"):
    newX = 607.5
    newY = 1080

# STEP 2: Create mp3 file of the text
text = "I (30M) have been seeing a woman (30F) for two months. We go out twice a week and I’ve noticed I’m always the one paying for dates (despite her insistence that she wants to be “equals” in a relationship). Last week we finally had sex and agreed to be official.Fast forward to last night: I took her out to dinner and when the bill came I asked if she’d be open to splitting it since we were serious now. She hesitantly took out her purse and paid her half. She was relatively quiet the rest of the evening and since I sensed something was off I didn’t push for intimacy. This morning I received a text from her saying, “Now that you got what you wanted I see your true colors.” I replied, “If you’re referring to splitting the bill, I felt it was only fair as we’re serious now. If you rather we take turns paying, that’s also fine with me. It doesn’t have to be exactly 50/50 but we make a similar income and I prefer a partnership of equals.” FWIW, we both make around $200K/yr. She said she couldn’t believe me and accused me of “tricking” her, saying I “used” her for sex and wasn’t a good person. I feel she overreacted to a reasonable request. Am I wrong to end things?"
voice = "en_us_006"

# arguments:
#   - input text
#   - voice which is used for the audio
#   - output file name
#   - play sound after generating the audio
tts(text, voice, "output.mp3")

# STEP 3: Figure out how long the tts is
ttsClip = AudioFileClip("output.mp3")
duration = ttsClip.duration
# STEP 4: Create a short version of the video clip that matches
#         the length of the audio

vid = VideoFileClip("bottom.mp4")
newVid = vid.set_duration(duration)

# STEP 5: Edit video to fit into tiktok screen

newVid = vfx.crop(newVid, x1=437.5,y1=0, width=405, height=720)

# STEP 6: Put the tts onto the video
newVid = newVid.set_audio(ttsClip)
newVid.write_videofile("movie.mp4")

# TESTING'''