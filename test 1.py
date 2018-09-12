# -*- coding: utf-8 -*-
"""
AUTHOR:Petrouchka Moise
DESCRIPTION: python text generator
LICENSE:General Public Liscense V2
"""

import random

#List of nouns
nouns = ["brooklyn",
        "staten island",
        "queens",
        "manhattan"]

#List of verbs
verbs = ["yells",
         "whispers",
         "cries",
         "talks"]



#list of adjectives
adjectives = ["pretty",
              "courageous",
              "deadly",
              "silly"]

#select random items from word list
random.seed()
noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)

#word poem
print "The "+adjective+" "+noun+"."


#for loop to iterate through verbs:
i=1
for verb in verbs:
    whitespace=" "*i
    print whitespace+verb
    i=i+1
    
#string formating
#print "The {adj} {n} {v}.".format(adj=adjective, n=noun, v=verb)


#for noun in nouns:
#    print nouns[i]
#    i=i+1


