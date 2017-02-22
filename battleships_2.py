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
    def __init__(self):
        self._ships = [[None for i in range(10)] for j in range(10)]
        mapa = generate_field()
        for i in range(len(mapa)):
            for j in range(len(mapa)):
                if mapa[i][0][j] == '*' or mapa[i][0][j] == 'X':
                    ship_pos =[(i, j)]
                    mapa[i][0] = mapa[i][0][:j] + '#' + mapa[i][0][(j + 1):]
                    a = b = c = d = size = 1
                    hor = True
                    for ij in range(3):
                        if i - a > -1:
                            if mapa[i - a][0][j] == '*' or mapa[i - a][0][j] == 'X':
                                mapa[i - a][0] = mapa[i - a][0][:j] + '#' + mapa[i - a][0][(j + 1):]
                                ship_pos.append((i - a, j))
                                a += 1
                                size += 1
                                hor = False
                        if i + b < 10:
                            if mapa[i + b][0][j] == '*' or mapa[i + b][0][j] == 'X':
                                mapa[i + b][0] = mapa[i + b][0][:j] + '#' + mapa[i + b][0][(j + 1):]
                                ship_pos.append((i + b, j))
                                b += 1
                                size += 1
                                hor = False
                        if j - c > -1:
                            if mapa[i][0][j - c] == '*' or mapa[i][0][j - c] == 'X':
                                mapa[i][0] = mapa[i][0][:(j - c)] + '#' + mapa[i][0][(j - c + 1):]
                                ship_pos.append((i, j - c))
                                c += 1
                                size += 1
                                hor = True
                        if j + d < 10:
                            if mapa[i][0][j + d] == '*' or mapa[i][0][j + d] == 'X':
                                mapa[i][0] = mapa[i][0][:(j + d)] + '#' + mapa[i][0][(j + d + 1):]
                                ship_pos.append((i, j + d))
                                d += 1
                                size += 1
                                hor = True
                    for ii in range(len(ship_pos)):
                        if hor is True:
                            self._ships[ship_pos[ii][0]][ship_pos[ii][-1]] = Ship(ship_pos[0], True, (1, size))
                        else:
                            self._ships[ship_pos[ii][0]][ship_pos[ii][-1]] = Ship(ship_pos[0], False, (size, 1))
                            
    def shoot_at(self, zil):
        if self._ships[zil[0]][zil[1]] is None:
            self._ships[zil[0]][zil[1]] = False
        elif self._ships[zil[0]][zil[1]] is True or self._ships[zil[0]][zil[1]] is False:
            print('You shot the same spot twice!')
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

