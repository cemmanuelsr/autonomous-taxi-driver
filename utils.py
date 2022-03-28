CODE_TO_LETTER_MAP = {
    0: b'R',
    1: b'G',
    2: b'Y',
    3: b'B'
}

MOVE_ACTION_MAP = {
              (1, 0): 1,
    (0, -2): 3,        (0, 2): 2,
              (-1, 0): 0
}

def find_row_col(desc, code):
    letter = CODE_TO_LETTER_MAP[code]
    for row in range(1, len(desc)-1):
        for col in range(1, len(desc[0])-1):
            if (desc[row][col] == letter):
                return row - 1, col // 2

class Entity:

    def __init__(self, row, col, name):
        self.row = row
        self.col = col
        self.name = name

class Taxi(Entity):

    def __init__(self, row, col):
        super(Taxi, self).__init__(row, col, name='Taxi')

class Passenger(Entity):

    def __init__(self, row, col, idx):
        self.idx = idx
        super(Passenger, self).__init__(row, col, name='Passenger')

class Destiny(Entity):
    def __init__(self, row, col, idx):
        self.idx = idx
        super(Destiny, self).__init__(row, col, name='Destiny')


def euclidian_distance(entity1, entity2):
    return ( (entity1.row - entity2.row)**2 + (entity1.col - entity2.col)**2 )**0.5

def manhattan_distance(entity1, entity2):
    return abs(entity1.row - entity2.row) + abs(entity1.col - entity2.col)
