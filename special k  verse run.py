# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:34:48 2018

@author: Windows 10 Pro
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:  text-to-audio.py
AUTHOR:  Petrouchka Moise
PURPOSE: Final project on digital culture
LICENSE: GNU General Public License v2
DEPENDENCIES: playsound and gTTs
"""

# import libraries
from playsound import playsound
from gtts import gTTS

# text to speech
tts = gTTS(text="""Have you Ever Loved My Special K,
           Whether you thought you were her Bae, Boo, or her Boy
           Wanting to believe that all she gave was all for you,
           My Special K bathed you with a smile
           that made you want to burrow more into her warm chest
           To drown in her ocean""",
           lang="en")

# write audio file
tts.save("../poems/Have-You-Ever-Loved-My-Special-K.mp3")

# play audio file
playsound("../poems/Have-You-Ever-Loved-My-Special-K.mp3")