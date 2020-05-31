#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:22:38 2020.
@author: john pappenheim

How to add to the game:
    1. Study the format of "rooms.append" in the file "locations.py".
    2. Add another room, by adding another "rooms.append" statement.
        change the "name", "description","connections","items","requirements","dark"
        to conform to your new room.
    3. If you have added any new "items" to your room,
        then you should add any synonyms for that word in
        the "synonyms" Dictionary in file "vocabulary.py".
    4. If you have added a Dictionary item key "requirement",
        the value of that Dictionary item should be a text message
        that is displayed when you are NOT carrying the requirement item.
"""
#import arcade
#import pyglet
import random
import locations
import vocabulary


DEBUG = False

things = locations.things
rooms = locations.rooms  # This is the list of all rooms.
verbs = vocabulary.verbs  # A Dictionary of Verbs (or commands), and their synonyms.
moves = vocabulary.moves  # A list of "directions" that you can move.
articles = vocabulary.articles  # A list of words that will be ignored.
here = rooms[0]  # This is the room you ae currently in.
# global my_items
my_items = []  # This is a list of everything you are carrying.

def debug(*text):
    """Use to printout information for debugging purposes."""
    if DEBUG:
        print("DEBUG: ", text)

def create_list_of_room_names():
    """Create a list of all the room names."""
    list_of_room_names = []
    for r in rooms:
        list_of_room_names.append(r.name)
    return list_of_room_names

def get_new_room(right_here, command):
    """Determine which room this command would take you to."""
    for i in right_here.connections:
        if i == command:
            room_name = right_here.connections.get(command)
            for room_number in range(len(rooms)):
                if rooms[room_number].name == room_name:
                    return rooms[room_number]
        continue
    print("There is no passage in that direction")
    return False

def look(here):
    """Display this room and it's contents."""
    here.look(my_items)

def show_inventory(my_items):
    """Display all of the items you are carrying."""
    if len(my_items) == 0:
        print("You are not carrying anything.")
        return
    print("You are carrying:")
    w = 0
    for i in my_items:
        print("    ", i.description)
        w = w + i.weight
    print("Total weight = ", w, "pound")

def take_item(list_of_items):
    """Attempt to pick up the items and carry them."""
    if "all" in list_of_items:
        debug(list_of_items)
        debug(here.items)
        this_rooms_items = here.items.copy()
        debug("this_rooms_items = ", this_rooms_items)
        i = 0
        for item in this_rooms_items:
            debug("item =  ", item.name)
            my_items.append(item)  # add the item to the player
            print("You pick up the", item.name)
            i = i + 1
        here.items.clear()  # remove all the items from the room
    else:
        debug("list_of_items = ", list_of_items)
        debug(here.items)
        list_of_items = list_of_items.copy()
        for item in list_of_items:
            if not get_item(item):
                txt = 'There is no "{}" here.'
                print(txt.format(item))
                continue
            item = get_item(item)
            if item in here.items:
                # It's here, take it
                my_items.append(item)  # add the item to the player
                here.items.remove(item)  # remove the item from the room
                print("You pick up the", item.name)
            else:
                txt = 'There is no "{}" here.'
                print(txt.format(item.name))

def drop_item(list_of_nouns):
    """Take item away from player and put it in this room."""
    if "all" in list_of_nouns:
        debug(my_items)
        my_items_copy = my_items.copy()
        for item in my_items_copy:
            here.items.append(item)  # add the item to the room
            print("You drop the", item.name)
        my_items.clear()  # remove all the items from the player
    else:
        debug("list_of_nouns = ", list_of_nouns)
        debug(here.items)
        for item in list_of_nouns:
            if not get_item(item):
                print("You're not carrying a", item)
                continue
            item = get_item(item)
            if item in my_items:
                # It's here, take it
                here.items.append(item)  # add the item to the room
                my_items.remove(item)  # remove the item from the players items
                print("You drop the", item.name)
            else:
                debug(item)
                print("You are not carrying the", item.name)
    return

def get_command(verb):
    """Ask the player to enter a command."""
    global command_line_split
    print()
    a_list_of_nouns = []
    commandline = ""
    while commandline == "":
        commandline = str(input("> "))
        commandline = commandline.strip("'")
        debug("Commandline == ", commandline)
        commandline = commandline.lower()
        command_line_split = commandline.split(",")
        command_line_split = commandline.split(" ")

    for word in command_line_split:
        word = word.strip()
        if word in articles:
            continue  # ignore articles. (Like: the, an, a, this etc.)
        if word in vocabulary.synonyms:
            word = vocabulary.synonyms[word]
        if word in verbs:
            verb = verbs[word]
        elif word in nouns:
            a_list_of_nouns.append(word)
        elif word in verbs:
            a_list_of_nouns.append(word)
        else:
            a_list_of_nouns.append(word)

    return verb, a_list_of_nouns

def enter_room(from_room, to_room):
    """Use this to move from one room to another."""
    # TODO: Check for special situations before entering room
    if to_room.name == "below grate":
        if locations.keys in my_items:
            if locations.keys.status == "unused":
                print("The grate is locked.")
                room = from_room
                return room
    if to_room.name == "branch":
        if get_item("rope") in from_room.items:
            print("You shimmy down the rope and drop off the bottom end of the rope \
and land precariously on the Branch below.")
        else:
            print("It's too far to just drop down to the Branch below.")
            return from_room
    if check_requirements_before_entering_room(to_room):
        room = to_room
        look(room)
        return room
    else:
        return from_room

def check_requirements_before_entering_room(to_room):
    """Check for special situations before entering room."""
    if len(to_room.requirements) == 0:
        return True  # no requirements
    for r in to_room.requirements:
        if r in my_items:
            print(to_room.requirements[r][1])
            return True
        else:
            print(to_room.requirements[r][0])
            return False
    return True

def get_item(name):
    """Return the Item with the specified name."""
    for item in locations.names_of_things:
        if item == name:
            for i in range(len(locations.things)):
                if locations.things[i].name == item:
                    return locations.things[i]
    else:
        return False

def get_room(name):
    """Return the object Room with the given text 'name'."""
    debug("name = ", name)
    for r in rooms:
        debug("r.name = ", r.name)
        if r.name == name:
            return r
        continue
    else:
        print(name, "is not a room name.")
        return False

def writeln(f, txt):
    f.write(str(txt) + "\n")
    return

def save(room):
    f = open("save_game.txt", "wt")
    for r in rooms:
        writeln(f, "ROOM:")
        writeln(f, r.name)
        writeln(f, "ITEMS:")
        if len(r.items) == 0 or r.items == [None]:
            writeln(f, "no_more")
        else:
            for i in r.items:
                writeln(f, i.name)
            writeln(f, "no_more")
        writeln(f, "VISITED:")
        writeln(f, r.visited)
    writeln(f, "done")
    writeln(f, "LAMP:")
    writeln(f, get_item("lamp").status)
    writeln(f, "MATCHES:")
    writeln(f, get_item("matches").status)
    writeln(f, "KEYS:")
    writeln(f, get_item("keys").status)
    writeln(f, "MY_ITEMS:")
    for item in my_items:
        if item != []:
            writeln(f, item.name)
    writeln(f, "no_more")
    writeln(f, "MY_ROOM:")
    writeln(f, room.name)
    writeln(f, "done")
    f.close()

def load_it(txt):
    debug(txt.strip())
    return (txt.strip())

def load_room(f):
    room_name = load_it(f.readline())
    if room_name == "deck":
        room_name = room_name
    word = ""
    word = load_it(f.readline())
    while word != "ROOM:" and word != "done":
        if word == "ITEMS:":
            get_room(room_name).items = []
            word = ""
            while word != "no_more":
                word = load_it(f.readline())
                if word == "none" or word == "no_more":
                    break
                if word == "ROOM:" or word == "done":
                    break
                item = get_item(word)
                get_room(room_name).items.append(get_item(word))
            word = load_it(f.readline())
        if word == "VISITED:":
            word = load_it(f.readline())
            get_room(room_name).visited = str(word)
        word = load_it(f.readline())
        continue
    return (word)

def load(room):
    global my_items
    f = open("save_game.txt", "rt")
    done = False
    while not done:
        word = load_it(f.readline())
        if word == "done":
            done = True
            break
        while word == "ROOM:":
            word = load_room(f)
        if word == "LAMP:":
            word = load_it(f.readline())
            get_item("lamp").status = word
        if word == "MATCHES:":
            word = load_it(f.readline())
            get_item("matches").status = word
        if word == "KEYS:":
            word = load_it(f.readline())
            get_item("keys").status = word
        if word == "MY_ITEMS:":
            my_items = []
            word = load_it(f.readline())
            while word != "no_more":
                my_items.append(get_item(word))
                word = load_it(f.readline())
        if word == "MY_ROOM:":
            word = load_it(f.readline())
            from_room = room
            debug(room.name)
            to_room = get_room(word)
            here = enter_room(from_room, to_room)

    return (here, my_items)

""" --------------------------------------------------------
    ********************************************************

    Begin playing the game here.

    ********************************************************
    --------------------------------------------------------
"""
room_names = create_list_of_room_names()
nouns = vocabulary.get_nouns(rooms)
turn_counter = 0
escape_turn_counter = 0

print("\n\n")
enter_room(here, here)
quit_game = False

""" The main game loop """

while not quit_game:
    turn_counter = turn_counter + 1
    escape_turn_counter = escape_turn_counter + 1
    verb, list_of_nouns = get_command(verb="")

    if verb == "":
        print("Huh ?")
        continue

    if verb == "quit":
        quit_game = True
        print("Game over man!")
        continue

    if verb == "go" and list_of_nouns == []:
        print("Which direction?")
        continue

    if verb in moves:
        if here.name == "branch" and verb == "down":
            print("The fall from the branch was too far to survive.")
            print("You have died!")
            quit_game = True
            break

        newroom = get_new_room(here, verb)
        if not newroom:
            continue
        here = enter_room(here, newroom)
        continue

    if verb == "look":
        here.visited = False
        look(here)
        continue

    if verb == "take":
        debug("list_of_nouns = ", list_of_nouns)
        take_item(list_of_nouns)
        continue

    if verb == "inventory":
        show_inventory(my_items)
        continue

    if verb == "drop":
        debug("list_of_nouns = ", list_of_nouns)
        drop_item(list_of_nouns)
        continue

    if verb == "xyzzy":
        if here.name == "livingroom":
            newroom = here.get_room("sewer")
            here = enter_room(here, newroom)
            continue
        if here.name == "sewer":
            newroom = here.get_room("livingroom")
            here = enter_room(here, newroom)
            continue

    if verb == "eat":
        # Eat something if you have it.
        if not list_of_nouns:
            print("What do you want to eat?")
            continue
        if "food" in list_of_nouns:
            if (locations.food in my_items) or (locations.food in here.items):
                hungry = False
                hungry_counter = 0
                print("Ahhh. The food is delicious, and gives you energy \
to continue on your adventure.")
                continue
            else:
                print("You don't have any food.")
                continue
        else:
            print("You can't eat that.")
            continue

    if verb == "go" and list_of_nouns == []:
        # Trying to go somewhere that doesn't make sense.
        print("Which direction?")
        continue

    if verb == "escape":
        if escape_turn_counter > 10:
            newroom = here.get_room(random.choice(room_names))
            here = enter_room(here, newroom)
            escape_turn_counter = 0
            continue
        else:
            print("Nothing happened right now.")
            continue

    if verb == "zoom":
        if len(list_of_nouns) > 0:
            if len(list_of_nouns) > 1:
                list_of_nouns[0] = list_of_nouns[0] + " " + list_of_nouns[1]
            if here.get_room(list_of_nouns[0]):
                new_room = here.get_room(list_of_nouns[0])
                room = new_room
                here = new_room
                continue

    if verb == "light":
        if locations.matches in my_items:
            locations.matches.status = int(locations.matches.status) - 1
            if locations.matches.status < 0:
                print("You are all out of matches.")
                my_items.remove(locations.matches)
            else:
                print("You have", str(locations.matches.status), "matches left.")
                if "lamp" in list_of_nouns:
                    if (locations.lamp in my_items) or \
                            (locations.lamp in here.items):
                        locations.lamp.status = "lit"
                        print("You have lit the lamp.")
                else:
                    print("You can't light that.")
        else:
            print("You can't light that.")
        continue

    if verb == "unlock":
        # if locations.keys in my_items:
        if "grate" in list_of_nouns:
            if here.name == "grate":
                if (locations.keys in my_items) or \
                        (locations.keys in here.items):
                    print("You use the keys to unlock the grate.")
                    locations.keys.status = "used"
            else:
                print("You can't unlock that.")
        else:
            print("You can't unlock that.")
        continue

    if verb == "read":
        if "book" in list_of_nouns:
            if (locations.book in my_items) or (locations.book in here.items):
                print("")
                print("  Reading book .......")
                print("It was the best of times, it was the worst of times, \
it was the age of wisdom, it was the age of foolishness, it was the epoch of \
belief, it was the epoch of incredulity, it was the season of light, it was \
the season of darkness, it was the spring of hope, it was the winter of \
despair...... Blah Blah Blah")
                print('......This book is too long to read the whole thing now. \
However, I see something written inside the front cover. It says:  \
Theres always an "escape"')
                continue
            else:
                print("There is nothing to read here.")
                continue
        else:
            print("You can't read that.")
            continue

    if verb == "save":
        save(here)
        continue

    if verb == "load":
        here, my_items = load(here)
        continue

    else:
        txt = "I don't know what {} is."
        for noun in list_of_nouns:
            print(txt.format(noun))
    continue
