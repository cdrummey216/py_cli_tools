import speech_recognition as sr
import sys
import os
import subprocess as sp
import time

##local vars##
fileName = str(sys.argv[1])
#fileName = "C:/Users/cdrum/Desktop/audio/a/segment.mp3"
flacFile = os.path.splitext(fileName)[0] + '.flac'
##local var

try:
    sp.call("ffmpeg -i " + fileName + " -compression_level 12 " + flacFile, shell = True)
except:
    print("ERROR: ffmpeg failed to convert the file.")
r = sr.Recognizer()
with sr.AudioFile(flacFile) as source:
    audio = r.record(source)

try:
    response_data = r.recognize_google(audio)
    with open("C:/Users/cdrum/Desktop/audio/all_notes.txt", "a") as f:
        f.write(str(fileName) + "\n" + response_data +"\n" + time.strftime("%Y%m%d-%H%M%S") +"\n")
    print("Success; Google thinks you said: " + response_data)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))