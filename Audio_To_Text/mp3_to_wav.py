# importing libraries to get audio
import os
from os import path
from pydub import AudioSegment

wav_num = 1

# files                                                                         
path ='E:\steven\kellylessons\Relationship Astrology Intro Course' 
os.chdir(path)

for mp3 in os.listdir(path):
    src = mp3 # the .mp4 file you're converting
    dst = "test" + str(wav_num)+ ".wav" # the name of the new .wav audio file you choose
    # convert wav to mp4                                                            
    sound = AudioSegment.from_file(src, format="mp3")
    sound.export(dst, format="wav")
    wav_num += 1