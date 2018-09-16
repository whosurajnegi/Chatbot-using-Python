from gtts import gTTS
import pyglet
import time, os

def tts(text1, lang):
    file = gTTS(text = text1, lang = lang)
    filename = 'C:/Users/admin/Desktop/Final/tmp/temp.mp3'
    file.save(filename)

    music = pyglet.media.load(filename, streaming = False)
    music.play()

    time.sleep(music.duration)
    os.remove(filename)