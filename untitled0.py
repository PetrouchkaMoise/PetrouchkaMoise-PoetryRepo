# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 19:31:25 2018

@author: Windows 10 Pro
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:  text-to-audio.py
AUTHOR:  Brendan Harmon <brendan.harmon@gmail.com>
PURPOSE: Open educational materials for a seminar on digital culture
LICENSE: GNU General Public License v2
DEPENDENCIES: playsound and gTTs
"""

# import libraries
from playsound import playsound
from gtts import gTTS

# text to speech
tts = gTTS(text="Hello world", lang="en")

# write audio file
tts.save("../poems/hello-world.mp3")

# play audio file
playsound("../poems/hello-world.mp3")