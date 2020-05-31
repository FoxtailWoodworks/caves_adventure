#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:34:06 2020.
All the rooms in the game
@author: johnpappenheim
"""
import vocabulary


class Item():
    """An item has a name, a description, a weight, and a status.

    The name is a short lower case noun describing the item.

    The description will automatically be prefixed with "There is "
    and postfixed with "here." when printed.

    The weight is an integer specifying the weight in pounds.

    The status is something that you can program a special case
    for it in the main loop in mycaves.py.
    """

    def __init__(self, name, description, weight, status):
        """Initialize the item."""
        self.name = name
        self.description = description
        self.weight = weight
        self.status = status


rope = Item("rope", "a coiled rope about 15 feet long.", 2, "")
boots = Item("boots", "a pair of brown hightop leather hiking boots.", 5, "")
lamp = Item("lamp", "an old Deitz oil lamp, full of oil.", 2, "unlit")
food = Item("food", "a brown paper bag with a balogna sandwich in it.", 2, "")
nuts = Item("nuts", "a small pile of hazel nuts.", 1, "")
matches = Item("matches", "a book of matches", 1, 10)  # 10 matches
book = Item("book", "a tattered leather bound book.", 3, "")
keys = Item("keys", "a ring of old brass skeleton keys.", 1, "unused")
foo = Item("foo","This item is a dummy and should not be put in any room", 0, "")

global things
things = [rope, boots, lamp, food, nuts, matches, book, keys]

global names_of_things
names_of_things = []
for item in things:
    names_of_things.append(item.name)


class Room():
    """Contain all information about a room."""

    def __init__(self, name, description, connections, items, requirements, dark):
        self.name = name
        self.description = description
        self.connections = connections
        self.items = items
        self.requirements = requirements
        self.dark = dark
        self.visited = False

    @staticmethod
    def get_item(name):
        """Return the Item with the specified name."""
        for a_thing in things:
            if a_thing.name == name:
                return a_thing

    def look(self, my_items):
        """Print out the description and items in this room."""
        print()
        ok = False
        if not self.dark:
            ok = True
        elif self.get_item("lamp") in my_items or self.get_item("lamp") in self.items:
            for a_item in my_items:
                if a_item == self.get_item("lamp"):
                    if a_item.status == "lit":
                        ok = True
        else:
            ok = False
        if ok:
            if self.visited == "False" or (not self.visited):
                print("---", self.name, "---")
                print(self.description)
                self.visited = True
                if len(self.items) != 0:
                    i_count = 0
                    for a_item in self.items:
                        itemname = self.items[i_count].description
                        print("There is", itemname, "here.")
                        i_count = i_count + 1
            else:
                print("---", self.name, "---")
            return
        print("It is dark. You can't see a thing.")

    @staticmethod
    def get_room(name):
        """Return the Room with the given name."""
        for r in rooms:
            if r.name == name:
                return r


rooms = []
#
# PORCH
#
rooms.append(Room("porch", "You are on the North Porch of a beautiful red house. \
From the outside this house looks lavish. It has been built with wheat \
colored bricks and has white pine wooden decorations. Small, octagon \
windows allow enough light to enter the home and have been added to the \
house in a fairly asymmetrical pattern.",
                  # connections
                  {"south": "livingroom"},
                  # items
                  [rope],
                  # requirements
                  {},
                  # dark
                  False))
#
# LIVINGROOM
#
rooms.append(Room("livingroom", "This small, rectangular livingroom has \
coordinating metal furniture.  The floor is poured and the walls are papered. \
Light is provided by table lamps.  The room is done in colors that remind \
you of a fruit salad and overall has an elegant look.  Among the first \
things one notices walking in is a collection of action figures.",
                  # connections
                  {"north": "porch",
                   "out": "porch",
                   "up": "attic",
                   "west": "kitchen",
                   "south": "study"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
# ATTIC
#
rooms.append(Room("attic", "You are in the attic.  It is like those in many \
dwellings in the neighbourhood in that it was tall and fully boarded. Sure it \
was difficult to stand right at the edges where the roof sloped down, but \
there was plenty of room even for the tallest of adults. But unlike the \
others rather than being full of junk it had been slept in every night for \
the winter months.",
                  # connections
                  {"down": "livingroom",
                   "out": "livingroom"},
                  # items
                  [lamp],
                  # requirements
                  {},
                  # dark
                  False))
#
# KITCHEN
#
rooms.append(Room("kitchen", "You are in the kitchen. It combines elegance \
and functionality, blending granite countertops and marble flooring with \
stainless steel appliances and glass-and-wood cabinets.",
                  # connections
                  {"east": "livingroom",
                   "south": "pantry"},
                  # items
                  [matches],
                  # requirements
                  {},
                  # dark
                  False))
#
# PANTRY
#
rooms.append(Room("pantry", "You are in a small room located near the kitchen,\
dedicated to food storage and/or storing kitchenware. Since the pantry is \
not typically temperature-controlled (unlike a refrigerator or root cellar), \
the foods stored in this pantry are shelf-stable staples such as grains, \
flours, and preserved foods.",
                  # connections
                  {"north": "kitchen"},
                  # items
                  [food],
                  # requirements
                  {},
                  # dark
                  False))
#
# STUDY
#
rooms.append(Room("study", "You are in a study room. The place one studies. \
This study room has a desk and book shelves. Well, there are a lot but two \
are significant. There is a couch in the one corner and a cool DIY lamp in \
another. There is a mini table for someone to keep some snacks.",
                  # connections
                  {"east": "bedroom",
                   "south": "backyard",
                   "north": "livingroom"},
                  # items
                  [book],
                  # requirements
                  {},
                  # dark
                  False))
#
# BEDROOM
#
rooms.append(Room("bedroom", "The room contains a small bed, neatly made, two\
straight-backed chairs, a washstand, a bureau--without any mirror--and a \
small table. There are no drapery curtains at the dormer windows, no pictures \
on the wall.",
                  # connections
                  {"north": "bathroom",
                   "west": "study"},
                  # items
                  [boots, keys],
                  # requirements
                  {},
                  # dark
                  False))
#
# BATHROOM
#
rooms.append(Room("bathroom", "This cramped, rectangular bathroom has a \
bathtub and sink with glass fixtures.  The sink is set into a stone counter.  \
The floor is tiled and the walls are painted and decorated with a wallpaper \
border.  Light is provided by ceiling lights.  The room is done in warm \
colors and overall has a quaint atmosphere.",
                  # connections
                  {"south": "bedroom"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
# BACKYARD
#
rooms.append(Room("backyard", "The backyard is a miniature woodland of \
holly trees and native shrubs, each of them trimmed as if they were green \
flames. To move about them is a sort of music, a poetry that cannot be \
spoken in words, yet is heard and calms everything that you are.",
                  # connections
                  {"south": "alley",
                   "north": "study",
                   "east": "tree"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
# ALLEY
#
rooms.append(Room("alley", "The alley is quaint and cobbled. The houses each \
side have walls that wobble ever so slightly, but is apparent in the strong \
morning light. It winds a little, arcing to the right and the heady scent \
of flowers drifts down from the many window boxes.",
                  # connections
                  {"north": "backyard",
                   "east": "grate"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
#  GRATE
#
rooms.append(Room("grate", "Ah yes, the infamous 'grate' leading down to the \
sewer system and beyond. It's about 3 feet square. The bars are about 2 \
inches apart, and it is locked with a sturdy brass lock.",
                  # connections
                  {"south": "below grate",
                   "down": "below grate",
                   "west": "alley"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
# BELOW GRATE
#
rooms.append(Room("below grate", "You are under the grate. Light shines \
through the bars leaving stripes of light and dark on the muddy ground under \
your feet.",
                  # connections
                  {"south": "sewer",
                   "north": "grate",
                   "up": "grate",
                   "east": "cave mouth"},
                  # items
                  [],
                  # requirements
                  {keys: ["The grate is locked.", "You unlock the grate with \
the brass skeleton keys you are carrying."]},
                  # dark
                  False))
#
# SEWER
#
rooms.append(Room("sewer", "You could feel the wall on your left and \
nothingness on your right. The first thing that hit you was the foul smell, \
which would now be impossible to forget, so was the horrible strength of its \
odour. It was dark, but not too dark. In a distance you could see a beam of \
light, and you happily thought of an opening somewhere, probably a manhole, \
that could let you out of this physical and mental mess.",
                  # connections
                  {"south": "slimy water",
                   "east": "tunnel",
                   "north": "below grate"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
# SLIMY WATER
#
rooms.append(Room("slimy water", "You find yourself knee deep in smelly slimy \
water. The water flows slowly to the south dimminishing in quantity as it \
goes.",
                  # connections
                  {"south": "cocooned",
                   "east": "homeless shelter",
                   "north": "sewer"},
                  # items
                  [],
                  # requirements
                  {boots: ["You refuse to go any farther in your bare \
feet.", "Since you are wearing the boots, you walk confidently through the \
shallow water."]},
                  # dark
                  True))
#
# COCOONED
#
rooms.append(Room("cocooned", "We rest, cocooned in the body of the earth, \
feeling the rock beneath our feet. In the darkness I feel my blood return to \
a comfortable warmth, my eyes as calm as they are in my nightly dreams. \
Water runs ever so cooly from the cave opening down fissures, feeding \
springs in other places. And in those moments without the noise or \
distractions of the world, in that pristine peace, I am me. Whatever waits \
out there, whatever we face, I'm ready.",
                  # connections
                  {"north": "slimy water"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  True))
#
# TUNNEL
#
rooms.append(Room("tunnel", "In the barely lit tunnel hemmed in by the \
perfect arching sandstone walls there is something almost gleaming ahead. \
It isn't giving out light, more like it catches it at certain angles and \
reflects a brownish red hue.",
                  # connections
                  {"west": "sewer"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  True))
#
# HOMELESS SHELTER
#
rooms.append(Room("homeless shelter", "The abandoned tunnel had been a drug den and \
homeless shelter for decades. It's once beautiful arched brick walls were \
covered in graffiti. The floor was littered with hypodermic needles, broken \
bottles and sewage. It was populated by the most desperate low-lifes, locked \
in their own dog-eat-dog existence. No-one in their right mind would go \
there without a hazmat suit and some serious weaponry.",
                  # connections
                  {"west": "slimy water",
                   "east": "TBD"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  True))
#
# CAVE MOUTH
#
rooms.append(Room("cave mouth", "It was a cave mouth of impenetrable blackness, \
as I stepped in I watched my shadow dissolve into the surrounding darkness. \
It was dank and the only sound was the dripping water.",
                  # connections
                  {"north": "morass",
                   "south": "below grate",
                   "east": "bat roosts"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  True))
#
# MORASS
#
rooms.append(Room("morass", "A grand broken statue in a dire morass marks \
the entrance to this cavern. Beyond the broken statue lies a modest, shady \
room. It's covered in ash, broken pottery and broken stone. \
Your lamp allows you to see rows of statues, worn down and mutilated by \
time itself.",
                  # connections
                  {"south": "cave mouth",
                   "north": "collapsed",
                   "east": "clammy area"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  True))
#
# COLLAPSED
#
rooms.append(Room("collapsed", "You continue onwards, deeper into the cave's \
darkness. You pass dozens of similar rooms and passages, most of which \
have collapsed or were dead ends to begin with.",
                  # connections
                  {"south": "morass",
                   "east": "clammy area"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  True))
#
# CLAMMY AREA
#
rooms.append(Room("clammy area", "Further ahead is a single path. Its twisted \
trail leads downwards and soon you enter a clammy area. Countless traps, \
swinging axes and other devices move all around. They're either still \
active, or just activated. What happened in this place?",
                  # connections
                  {"west": "collapsed",
                   "south": "morass"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  True))
#
# BAT ROOSTS
#
rooms.append(Room("bat roosts", "The cavern wormed its way half a mile into \
the mountain. It's general shape was ovoid, the walls below the ridge \
smoothly curved to the floor, the walls above arched another hundred feet \
up to giant stalactites and the bat roosts.",
                  # connections
                  {"west": "cave mouth"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  True))

#
# TREE
#
rooms.append(Room("tree", "There in the centre of a million grassy wands stands a tree, \
her bark so patterned as if carved by her own rain-born flash rivers. She stretches up, \
as if so proud to stand there under the sun in any weather. How I wish she could see \
her own beauty, her green bounty and earthy browns, yet perhaps I should wish for her \
peace and the wisdom to simply be what I am.",
                  # connections
                  {"west": "backyard",
                   "up": "treehouse"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
# TREEHOUSE
#
rooms.append(Room("treehouse", "As you climb the stairs into the Treehouse, the first thing that \
strikes you is the stunning vista – looking out towards the blue seas of Chole Bay, framed by \
mangroves, vines and the majestic baobab which dominates the sundeck. Lie back on the king-sized \
bed and ease into island life by watching the white-sailed dhows float past and the fish eagles \
and kites soar in the sky. After a day of enjoying excursions relax under the hot shower which is \
nestled in a creaking bamboo thicket.",
                  # connections
                  {"down": "tree",
                   "east": "deck"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
# DECK
#
rooms.append(Room("deck", "This is a nice deck with a smooth maple floor \
and rough pine railing. The view from here is magnificent. Below you is \
a sturdy looking branch.",
                  # connections
                  {"west": "tree",
                   "down": "branch"},
                  # items
                  [],
                  # requirements
                  {},
                  # dark
                  False))
#
# BRANCH
#
rooms.append(Room("branch", "You are balancing precariously on a branch \
that's not quite as sturdy as it looked from above.  Be very careful.",
                  # connections
                  {"up":"rope_too_short"},
                  # items
                  [nuts],
                  # requirements
                  {},
                  # dark
                  False))
#
# ROPE_TOO_SHORT
#
rooms.append(Room("rope_too_short", "You are balancing precariously on a branch \
that's not quite as sturdy as it looked from above.  Be very careful.",
                  # connections
                  {},
                  # items
                  [],
                  # requirements
                  {foo:["The rope is too short for you to reach from down here"]},
                  # dark
                  False))

number_of_rooms = 0
for i in rooms:
    number_of_rooms = number_of_rooms + 1
