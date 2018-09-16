from gtts import gTTS                                                                 # importing google text-to-speech API
import pyglet                                                                         # importing pyglet for audio playback decoding 
import time, os                                                          

def tts(text, lang):                                                                  # defining variable 'text'  and 'lang'
    file = gTTS(text = text, lang = lang)
    filename = 'C:/Users/admin/Desktop/Final/tmp/temp.mp3'     # Store the converted file into a temporary folder 
    file.save(filename)

    music = pyglet.media.load(filename, streaming = False)                            # its decode the saved file and load it 
    music.play()                                                                      # music.play() plays the saved audio

    time.sleep(music.duration)
    os.remove(filename)                                                               # temporary speech file is removed