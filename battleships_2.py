class Ship:
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self._length = length
        if horizontal is True:
            self._hit = [False] * length[-1]
        else:
            self._hit = [False] * length[0]

    def shoot_at(self, zil):
        if self.horizontal is False:
            damaged_spot = zil[0] - self.bow[0]
        else:
            damaged_spot = zil[-1] - self.bow[-1]
        self._hit[damaged_spot] = True

class Player:
    def __init__(self, pl_name):
        self.pl_name = pl_name

    def read_position(self):
        while True:
            pos = input(self.pl_name + ', enter the coordinates: ')
            if pos[0].isalpha() and pos[1:].isdigit():
                break
            else:
                print('You entered wrong coordinates')
        if pos[0].isupper():
            spot = (int(pos[1:]) - 1, ord(pos[0]) - 65)
        else:
            spot = (int(pos[1:]), ord(pos[0]) - 97)
        return spot


class Field:
    def __init__(self, ships):
        #self._ships = [[Ship(self.bow), Ship(self.horizontal), Ship(self.length), Ship(self.hit)]])
        self._ships = [[' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10], [' '*10]]

    def shoot_at(self, zil):
        self._ships[zil[0]][0] = self._ships[zil[0]][0][:zil[1]] + '•' + self._ships[zil[0]][0][zil[1] + 1:]