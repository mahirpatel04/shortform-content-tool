from functions import Video

#----------------------------------------------------------
#                   MAIN DRIVER PROGRAM
#   Pick type of video, pick assests, generate video
#
#----------------------------------------------------------

link = "https://www.youtube.com/watch?v=HRt7QaPWEZc"
ttsFile = "sources/test.txt"
outputFile = "output/final.mp4"

vid = Video.combinedProcessing(outputFile, link, ttsFile)


