# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:33:35 2018

@author: Windows 10 Pro
"""
# import libraries
import markovify 

"""
Combine text from Kaiya Smith's Letter to Hansel and F*ckboys
"""
# get raw text as string
with open("../poems/HashtagHansel.txt") as f:
    Hansel = f.read()

with open("../poems/Fboi.txt") as f:
    boys = f.read()

# build and combine the models
Hansel_model = markovify.Text(Hansel)
boys_model = markovify.Text(boys)
model_synthesis = markovify.combine([Hansel_model, boys_model], 
    [ 1.5, 1 ])

# print five randomly-generated sentences
for i in range(5):
    print model_synthesis.make_sentence()
    
    