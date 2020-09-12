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
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'

SCREEN_WIDTH = 80


def over_world_location(coordinate):
    over_world_location_name = {
        -4.0: 'Keh Namut Shrine',
        0.0: 'Shrine of Resurrection',
        1.-4: 'Owa Daim Shrine',
        1.0: '1,0',
        2.0: 'Temple of Time',
        3.0: '3,0',
        3.4: 'Oman Au Shrine',
        4.2: 'Great Plateau Tower',
        6.0: 'Ja Baij Shrine',
    }
    return over_world_location_name.get(coordinate, "Location does not exist")


worldLocations = {
    over_world_location(0.0): {
     DESC: "Your place of awakening.",
     GROUND: ['Sheikah Slate']
    }
}


def displayLocation(loc):
    print(loc)
    print('=' * len(loc))


displayLocation(over_world_location(0.0))
