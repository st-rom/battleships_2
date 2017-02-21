from generator import *
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
        self._ships = [[None for i in range(10)] for j in range(10)]
        mapa = generate_field()
        for i in
    def shoot_at(self, zil):
        #self._ships[zil[0]][0] = self._ships[zil[0]][0][:zil[1]] + '•' + self._ships[zil[0]][0][zil[1] + 1:]
        if self._ships[zil[0]][zil[1]] is None:
            self._ships[zil[0]][zil[1]] = False
        else:
            self._ships[zil[0]][zil[1]] = True

    def field_without_ships(self):
        for i in range(len(self._ships)):
            for j in range(len(self._ships[i])):
                if self._ships[i][j] is True:
                    self._ships[i][j] = 'X'
                elif self._ships[i][j] is False:
                    self._ships[i][j] = '•'
                else:
                    self._ships[i][j] = ' '
        for i in range(len(self._ships)):
            self._ships[i] = ''.join(self._ships[i])
        self._ships = '\n'.join(self._ships)
        return self._ships

    def field_with_ships(self):
        for i in range(len(self._ships)):
            for j in range(len(self._ships[i])):
                if self._ships[i][j] is True:
                    self._ships[i][j] = 'X'
                elif self._ships[i][j] is False:
                    self._ships[i][j] = '•'
                elif self._ships[i][j] is None:
                    self._ships[i][j] = ' '
                else:
                    self._ships[i][j] = '*'
        for i in range(len(self._ships)):
            self._ships[i] = ''.join(self._ships[i])
        self._ships = '\n'.join(self._ships)
        return self._ships


class Game:
    def __init__(self, field, players, current_player):
        pl1 = input('Player 1, enter your name: ')
        pl2 = input('Player 2, enter your name: ')
        self._field = [Field(), Field()]
        self._players = [Player(pl1), Player(pl2)]
        self._current_player = 0

    def read_position(self):
        pos = Player.read_position()
        return pos

    def field_without_ships(self):
        print(self._field[self._current_player].field_with_ships())

    def field_with_ships(self):
        print(self._field[self._current_player].field_with_ships())

