#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:13:31 2020.
All the words that the user can type
@author: john pappenheim

"""


# A Dictionary of Verbs (or commands), and their synonyms.
verbs = {    "go"       :"go",
             "move"     :"go",
             "jump"     :"go",
             "crawl"    :"go",
             "climb"    :"go",
             "n"        :"north",
             "north"    :"north",
             "s"        :"south",
             "south"    :"south",
             "e"        :"east",
             "east"     :"east",
             "w"        :"west",
             "west"     :"west",
             "u"        :"up",
             "up"       :"up",
             "uphill"   :"up",
             "d"        :"down",
             "down"     :"down",
             "in"       :"in",
             "out"      :"out",
             "i"        :"inventory",
             "inventory":"inventory",
             "take"     :"take",
             "get"      :"take",
             "drop"     :"drop",
             "put"      :"drop",
             "q"        :"quit",
             "quit"     :"quit",
             "exit"     :"quit",
             "l"        :"look",
             "look"     :"look",
             "xyzzy"    :"xyzzy",
             "escape"   :"escape",
             "light"    :"light",
             "eat"      :"eat",
             "unlock"   :"unlock",
             "read"     :"read",
             "zoom"     :"zoom",
             "save"     :"save",
             "load"     :"load",
             }

# A list of "directions" that you can move.
moves = ["north","south","east","west","up","down","in","out"]

# A list of words that will be ignored.
articles = ["the","an","a","and","this","that","those","these","them","his","hers","my","mine"]

# In this Dictionary,
# if the lefthand "key"" is typed, it will be replaced by the righthand "value"".
synonyms ={"everything":    "all",
           "shoes":         "boots",
           "galoshes":      "boots",
           "lantern":       "lamp",
           "deitz":         "lamp",
           "roop":          "rope",
           "line":          "rope",
           "bag":           "food",
           "sack":          "food",
           "sandwich":      "food",
           "nuts":          "nuts",
           "keys":          "keys",
           "key":           "keys",
           }


def get_nouns(rooms):
    """Create a list of nouns from the items in all the rooms."""
    nouns = []
    for r in rooms:
        if len(r.items) > 0:
            for key in r.items:
                nouns.append(key)
    return nouns

