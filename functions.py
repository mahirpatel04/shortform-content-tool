from pytube import YouTube
from moviepy.editor import *
from tiktokvoice import tts
import os.path

def downloadVideo(link, fileName):
    """
    Given youtube link, download video as specified filename and return resolution

    Args:
        link : link to download (str)
        fileName: name to store the download as (str)
        
    Return:
        resolution of video: int
    """
    yt = YouTube(link)
    videoStreams = yt.streams.filter(adaptive=True, file_extension="mp4", type="video")
    max = int(videoStreams[0].resolution[:-1:])
    key = 0
    for i in range(len(videoStreams)):
        if int(videoStreams[i].resolution[:-1:]) == 1080:
            videoStreams[i].download(filename=fileName)
            return 1080
        elif int(videoStreams[i].resolution[:-1:]) > max:
            max = videoStreams[i].resolution[:-1:]
            key = i
    videoStreams[key].download(filename=fileName)
    return max
  
def setVideoResolution(originalRes):
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

def createTTS(fileNameInput, fileNameOutput, voice="en_us_006"):
    """
    Creates the TTS mp3 file
    
    Args:
        fileNameInput: name of the text file to read from (str)
        voice: the voice of the reader (str)
        fileNameOutput: mp3 file will be saved as this (str)
    
    Return:
        None
    """
    if os.path.isfile("./" + fileNameInput):
        file = open(fileNameInput, "r")
        text = file.read()
    else:
        raise Exception("Script file not found in current directory")
    
    tts(text, voice, fileNameOutput)
    
def edit(audioFileName, backgroundFileName, originalRes, outputFileName):
    """
    Stitches together the audio and bg video after cropping
    
    Args:
        audioFileName: file name for the TTS mp3 (str)
        backgroundFileName: file name for the background mp4 (str)
        originalRes: originalResolution of the bg video (int)
        outputFileName: video will be stored with this name (str)
    
    Return:
        None
    """
    
    # Set width and height of the video
    width, height = setVideoResolution(originalRes)
    
    # Figure out how long the audio is
    ttsClip = AudioFileClip(audioFileName)
    duration = ttsClip.duration
    
    # Create a short version of the video to match the audio
    vid = VideoFileClip(backgroundFileName)
    vid = vid.set_duration(duration)

    # Edit video to fit into tiktok screen
    x1 = ((height * 16)/9 - width)/2
    vid = vfx.crop(vid, x1=x1, y1=0, width=width, height=height)

    # Put the tts onto the video
    vid = vid.set_audio(ttsClip)
    vid.write_videofile(outputFileName)
    
    return

