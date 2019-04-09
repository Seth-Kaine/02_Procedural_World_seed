#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2019 seth <seth@Deeper>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from seed import generate_seed
from make_noise import simplex, randomly_populate_map
from render_engine import *

w = 150
h = 100
class Tile:
    #a tile of the map and its properties
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
 
        #by default, if a tile is blocked, it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight
 
def make_map():
    global map
 
    #fill map with "unblocked" tiles
    map = [
         [Tile(False) for y in range(h)]
         for x in range(w) 
    ]
    
    
    map = randomly_populate_map(map,seed, (w,h),1.2,6.0)
 
    #place two pillars to test the map
    """
    map[30][22].blocked = True
    map[30][22].block_sight = True
    map[10][22].blocked = True
    map[10][22].block_sight = True
    map[11][22].blocked = True
    map[11][22].block_sight = True
    """


def main(args):
    global seed
    msg = 'mySeed : %s'
    try:
        mySeed = args[1]
    except:
        mySeed = 25
    if mySeed == 25:
        msg = 'The Default mySeed : %s'
    print(msg % mySeed)
    seed = generate_seed(mySeed)
    #print(args['seed'])
    global h
    global w
    #h = 3
    #w = 3
    
    
    #print(repr(map))
    
    #display_map(map)
    #generate map (at this point it's not drawn to the screen)
    make_map()
     
     
    while not libtcod.console_is_window_closed():
     
        #render the screen
        render_all(map)
     
        libtcod.console_flush()
     
        #erase all objects at their old locations, before they move
        for object in objects:
            object.clear()
     
        #handle keys and exit game if needed
        exit = handle_keys()
        if exit:
            break
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
