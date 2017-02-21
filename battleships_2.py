class Ship():
    bow
    horizontal
    hit
    def __init__(length):
        self.length = length
    def shoot_at(tupl):
        if mapa[tupl[0]][0][tupl[-1]] == '*':
            print('You shot the ship!!!')


class Player:
    def __init__(self, pl_name):
        self.pl_name = pl_name
    def read_position(pos):
        if pos[0].isupper():
            spot = (int(pos[1:]) - 1, ord(pos[0]) - 65)
        else:
            spot = (int(pos[1:]), ord(pos[0]) - 97)
        return spot


class Field:
    def __init__(self, ships):
        self.ships = Ship([[Ship()]])