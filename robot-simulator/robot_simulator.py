NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):

    INSTRUCTION_TO_FUNCTION_MAP = {
        'A': 'advance',
        'L': 'turn_left',
        'R': 'turn_right',
    }

    def __init__(self, bearing=NORTH, pos_x=0, pos_y=0):
        self.bearing = bearing
        self.pos_x = pos_x
        self.pos_y = pos_y

    @property
    def coordinates(self):
        return self.pos_x, self.pos_y

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def advance(self):
        if self.bearing == NORTH:
            self.pos_y += 1
        elif self.bearing == EAST:
            self.pos_x += 1
        elif self.bearing == SOUTH:
            self.pos_y -= 1
        elif self.bearing == WEST:
            self.pos_x -= 1

    def simulate(self, sequence):
        for instruction in sequence:
            fn_name = self.INSTRUCTION_TO_FUNCTION_MAP[instruction]
            getattr(self, fn_name)()
