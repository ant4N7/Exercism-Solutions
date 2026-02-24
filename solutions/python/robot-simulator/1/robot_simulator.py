EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (x_pos,y_pos)

    def rotate(self,instruction):
        if instruction == 'R':
            self.direction = (self.direction - 90)%360
        if instruction == 'L':
            self.direction = (self.direction + 90)%360

    def move(self,instrucions):
        for instruction in instrucions:
            if instruction in 'LR': self.rotate(instruction)
            if instruction == 'A':
                if self.direction == EAST: self.x_pos += 1
                if self.direction == NORTH: self.y_pos += 1
                if self.direction == WEST: self.x_pos -= 1
                if self.direction == SOUTH: self.y_pos -= 1
        self.coordinates = (self.x_pos,self.y_pos)
