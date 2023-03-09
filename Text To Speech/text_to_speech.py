# Read in a text.txt file and convert to speech
# google Text to Speech API to convert your written Text to AI bot voice
# It can be choose the language type when generating the sound file
# By Samuel Ko

from pygame import mixer
# Google Text to Speech API gTTS (Google Text-to-Speech)
# Check the language support list by typing "gtts-cli --all" in terminal
from gtts import gTTS
import os  
import traceback

def txt_to_speech():
   try:
      input_file = input("Input your text file name : ")

      # Break down the file name into 'name' and 'extension'
      split_tup = os.path.splitext(input_file)
      # extract the file name and extension
      f_name = split_tup[0]
      f_extension = split_tup[1]
      
      print(f"File Name: {input_file} is now processing......")

      # Read the text file
      with open(input_file) as file_handle:
         data = file_handle.read()

      # tts = gTTS(data,lang='zh-TW')
      tts = gTTS(data,lang='en')

      # Set output file name
      o_file = f_name + ".mp3"
      tts.save(o_file)
      print(f"Conversion finished!")
      mixer.init()
   except RuntimeError:
      traceback.print_exc()

if __name__ == "__main__":
   txt_to_speech()
