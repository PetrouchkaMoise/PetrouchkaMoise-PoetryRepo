# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#import libraries
#from playsound import playsound
#from gtts import gTTS

#text to speech
#tts = gTTS(text="Tree in the land of bushes", lang="en")

#write audio file
#tts.save ("Tree in the land of bushes.mp3")
#play audio file
#playsound("Tree in the land of bushes.mp3")

# import libraries
from playsound import playsound
from gtts import gTTS
import markovify

# get raw text as string
with open("../poems/mallarme-a-roll-of-the-dice.txt") as f:
    text = f.read()

# build the markov model
text_model = markovify.NewlineText(text)

# print a randomly-generated sentence of no more than 140 characters
markov_poem = text_model.make_short_sentence(140)

# text to speech
tts = gTTS(text=markov_poem, lang='en')

# write audio file
tts.save("../poems/markovified-poem.mp3")

# play audio file
playsound("../poems/markovified-poem.mp3")