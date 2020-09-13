
import textwrap

DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
ROOMDESC = 'roomdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'


SCREEN_WIDTH = 80

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Converting xy coordinate values to location names via switch case \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def worldLocation(coordinate):
    worldLocationName = {
        -5.1: 'River of the Dead',
        -4.1: 'River of the Dead',
        -4.0: 'Keh Namut Shrine',
        -3.4: 'Forest of Spirits',
        -3.3: 'Hopper Pond',
        -2.4: 'Forest of Spirits',
        -2.3: 'Forest of Spirits',
        -1.4: 'Forest of Spirits',
        -1.3: 'Forest of Spirits',
        -1.2: 'Forest of Spirits',
        0.0: 'Shrine of Resurrection',
        0.2: 'Forest of Spirits',
        0.3: 'Forest of Spirits',
        0.4: 'Forest of Spirits',
        1.-4: 'Owa Daim Shrine',
        1.3: 'Forest of Spirits',
        2.0: 'Temple of Time',
        3.-2: 'Mount Hylia',
        3.4: 'Oman Au Shrine',
        4.2: 'Great Plateau Tower',
        6.0: 'Ja Baij Shrine',
    }
    return worldLocationName.get(coordinate, "Location does not exist")

def worldLocationRoom(roomIdValue):
    worldLocationRoomName = {
        0: 'Bed Chamber',
        1: 'Lobby',
    }
    return worldLocationRoomName.get(roomIdValue, "Room does not exist")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# List of World locations and their properties \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

worldLocations = {
    worldLocation(0.0): {
        worldLocationRoom(0): {
            ROOMDESC: "This chamber holds the stone tub from which you awoke. It was once filled with a mysterious "
                      "blue liquid.",
            GROUND: ['Sheikah Slate']
        },
        worldLocationRoom(1): {
            ROOMDESC: "This room is quite large. It's walls are that of a smooth patterned black stone, with ornate "
                      "pillars in the corner."
        },
        DESC: "Your place of awakening."
    }
}

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Displaying/accessing area properties \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# displayLocation(overWorldLocation(coordinate)

def displayLocation(worldlocation, worldlocationroom):

    # Print location name with fancy divider
    print("Location: " + worldlocation)
    print('=' * len("Location: " + worldlocation))
    print("Room: " + worldlocationroom)
    print('=' * len("Room: " + worldlocationroom))

    # Print location description with textwrap.wrap()
    print('\n'.join(textwrap.wrap(worldLocations[worldlocation][DESC], SCREEN_WIDTH)))
    print('*' * len(worldLocations[worldlocation][DESC]))

    # Print room description with textwrap.wrap()
    print('\n'.join(textwrap.wrap(worldLocations[worldlocation][worldlocationroom][ROOMDESC], SCREEN_WIDTH)))


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Test:
displayLocation(worldLocation(0.0), worldLocationRoom(0))
