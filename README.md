# Python 3.7 Command Line Tools

## Transcribe Audio using [Google's Cloud Speech to Text](https://cloud.google.com/speech-to-text/)

### segmented.py
creates subfolder of <60sec segments (api limitations) of the audio file and writes response to new transcript.txt;

usage: python segmented.py path/to/audio/file
output: writes response to transcript.txt;

### transcribe.py
converts mp3 file to .flac using ffmpeg and then transcribes using Google's Cloud Speech to Text

usage: python transcribe.py path/to/audio/file_segment
output: appends to existing all_notes.txt file with date of recording and transcribed text
