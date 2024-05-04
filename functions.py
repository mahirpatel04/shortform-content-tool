from pytube import YouTube
from moviepy.editor import *
from tiktokvoice import tts
import os.path
import random
class File:
    def __init__(self, fileName):
        self.fileName = fileName

class Video(File):
    def __init__(self, fileName, res):
        super().__init__(fileName)
        self.res = res
        
    @classmethod      
    def fromLink(self, outputFileName, link):
        """
        Given youtube link, download video as specified filename and return resolution

        Args:
            link : link to download (str)
            fileName: name to store the download as (str)
            
        Return:
            resolution of video: int
        """
        if os.path.exists(outputFileName):
            raise FileExistsError("File Already Downloaded")
        
        yt = YouTube(link)
        videoStream = yt.streams.get_highest_resolution()
        res = int(videoStream.resolution[:-1:])
        videoStream.download(filename=outputFileName)
        
        return Video(outputFileName, res)
    
    @classmethod
    def combinedProcessing(self, fileName, bgVidLink, scriptFileName):
        try:
            vid = Video.fromLink("sources/bgVid.mp4", bgVidLink,)
        except FileExistsError:
            print("Vid already existed, so did not re-download")
            vid = Video("sources/bgVid.mp4", 720)

        # Check if TTS is already created or not
        try:
            tts = Audio.fromTTSAudio("output/temp.mp3", scriptFileName,)
        except FileExistsError:
            print("TTS already existed, so did not re-download")
            tts = Audio("output/temp.mp3")


        # Check if Base Video is already created or not
        try:
            shortVid = Video(fileName, vid.res)
            videoClip = vid.stitch(tts.fileName, vid.fileName, fileName, vid.res)
            videoClip.write_videofile(fileName, audio_codec='aac')
            os.remove("output/output.aac")
            os.remove("output/temp.mp3")
            return shortVid
        except FileExistsError:
            print("Final video already exists, new one NOT CREATED")
            return

    def stitch(self, audioFileName, backgroundFileName, outputFileName, originalRes=720):
        if os.path.exists(outputFileName):
            raise FileExistsError("Output already exists")
        # Set width and height of the video

        width, height = self.getVideoResolution(originalRes)
        
        # Convert the audio to AAC
        originalAudio = AudioFileClip(audioFileName)
        originalAudio.write_audiofile("output/output.aac", codec="aac")
        ttsClip = AudioFileClip("output/output.aac")
        
        # Figure out how long the audio is
        duration = ttsClip.duration
        
        # Create a short version of the video to match the audio
        vid = VideoFileClip(backgroundFileName)
        vidDuration = vid.duration 
        vidEnd = random.randrange(int(duration), int(vidDuration))
        vidStart = vidEnd - duration
        vid = vid.subclip(vidStart, vidEnd)

        # Edit video to fit into tiktok screen
        x1 = ((height * 16)/9 - width)/2
        vid = vfx.crop(vid, x1=x1, y1=0, width=width, height=height)

        # Put the tts onto the video
        vid = vid.set_audio(ttsClip)
        originalAudio.close()
        return vid

    def getVideoResolution(self, originalRes):
        """
        Returns the width and height of the final video 
        that is going to be created
        
        Args:
            originalRes: resolution of the original video (int)
        
        Return:
            width: width of final video
            height: height of the final video
        
        """
        return (originalRes * 9 / 16), originalRes
               
class Audio(File):
    def __init__(self, outputFileName):
        super().__init__(outputFileName)
    @classmethod
    def fromTTSAudio(self, outputFileName, ttsInputFileName, voice="en_us_006"):
        if os.path.exists(outputFileName):
            raise FileExistsError("File Already Downloaded")
    
        if os.path.exists(ttsInputFileName):
            file = open(ttsInputFileName, "r")
            text = file.read()
        else:
            raise FileNotFoundError("Script file not found in current directory")
        
        tts(text, voice, outputFileName)
        
        file.close()
        return Audio(outputFileName)
