from generator import *
import os


class Ship:
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self._length = length
        if horizontal is True:
            self._hit = [False for i in range(length[-1])]
        else:
            self._hit = [False for i in range(length[0])]

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
            if 1 < len(pos) < 4:
                if pos[0].isalpha() and pos[1:].isdigit():
                    break
            else:
                print('You entered wrong coordinates')
        if pos[0].isupper():
            spot = (int(pos[1:]) - 1, ord(pos[0]) - 65)
        else:
            spot = (int(pos[1:]) - 1, ord(pos[0]) - 97)
        return spot


class Field:
    def __init__(self):
        self._ships = [[None for i in range(10)] for j in range(10)]
        self.mapa = generate_field()
        self.counter = 0
        self.strships = ''
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa)):
                if self.mapa[i][0][j] == '*' or self.mapa[i][0][j] == 'X':
                   # self.counter += 1
                    ship_pos =[(i, j)]
                    self.mapa[i][0] = self.mapa[i][0][:j] + '#' + self.mapa[i][0][(j + 1):]
                    a = b = c = d = size = 1
                    hor = True
                    for ij in range(3):
                        if i - a > -1:
                            if self.mapa[i - a][0][j] == '*' or self.mapa[i - a][0][j] == 'X':
                                self.mapa[i - a][0] = self.mapa[i - a][0][:j] + '#' + self.mapa[i - a][0][(j + 1):]
                                ship_pos.append((i - a, j))
                                a += 1
                                size += 1
                                hor = False
                    #            self.counter += 1
                        if i + b < 10:
                            if self.mapa[i + b][0][j] == '*' or self.mapa[i + b][0][j] == 'X':
                                self.mapa[i + b][0] = self.mapa[i + b][0][:j] + '#' + self.mapa[i + b][0][(j + 1):]
                                ship_pos.append((i + b, j))
                                b += 1
                                size += 1
                                hor = False
                     #           self.counter += 1
                        if j - c > -1:
                            if self.mapa[i][0][j - c] == '*' or self.mapa[i][0][j - c] == 'X':
                                self.mapa[i][0] = self.mapa[i][0][:(j - c)] + '#' + self.mapa[i][0][(j - c + 1):]
                                ship_pos.append((i, j - c))
                                c += 1
                                size += 1
                                hor = True
                      #          self.counter += 1
                        if j + d < 10:
                            if self.mapa[i][0][j + d] == '*' or self.mapa[i][0][j + d] == 'X':
                                self.mapa[i][0] = self.mapa[i][0][:(j + d)] + '#' + self.mapa[i][0][(j + d + 1):]
                                ship_pos.append((i, j + d))
                                d += 1
                                size += 1
                                hor = True
                       #         self.counter += 1
                    
                    if hor is True:
                        examp = Ship(ship_pos[0], True, (1, size))
                        for ii in range(len(ship_pos)):
                            self._ships[ship_pos[ii][0]][ship_pos[ii][-1]] = examp
                    else:
                        examp = Ship(ship_pos[0], False, (size, 1))
                        for ii in range(len(ship_pos)):
                            self._ships[ship_pos[ii][0]][ship_pos[ii][-1]] = examp
                        
        self.di = {}
        for i in range(10):
            for j in range(10):
                if self._ships[i][j]:
                    self.di[self._ships[i][j]]  = self.di.get(self._ships[i][j],0) + 1
        print(self.di)
    def shoot_at(self, zil):
        if self._ships[zil[0]][zil[1]] is None:
            self._ships[zil[0]][zil[1]] = False
        elif self._ships[zil[0]][zil[1]] is True or self._ships[zil[0]][zil[1]] is False:
            print(' You shot the same spot twice!')
        else:
            self._ships[zil[0]][zil[1]].shoot_at(zil)
            infa = self._ships[zil[0]][zil[1]]
            self._ships[zil[0]][zil[1]] = True
 #       print(self._ships[zil[0]][zil[1]])
            self.counter += 1
            print(' Nice! Shoot again!')
            return infa
        print(' Missed')
        return self._ships[zil[0]][zil[1]]

    def field_without_ships(self):
        strships = [[' ' for i in range(10)] for j in range(10)]
        strships.insert(0, '  ABCDEFGHIJ')
        for i in range(len(self._ships)):
            for j in range(len(self._ships[i])):
                if self._ships[i][j] is True:
                    strships[i + 1][j] = 'X'
                elif self._ships[i][j] is False:
                    strships[i + 1][j] = '•'
                else:
                    strships[i + 1][j] = ' '
        for i in range(len(self._ships)):
            strships[i + 1] = ''.join(strships[i + 1])
            if i + 1 < 10:
                strships[i + 1] = ' ' + str(i + 1) + strships[i + 1]
            else:
                strships[i + 1] = str(i + 1) + strships[i + 1]
        strships = '\n'.join(strships)
        return strships

    def field_with_ships(self):
        strshipsw = [[' ' for i in range(10)] for j in range(10)]
        strshipsw.insert(0, '  ABCDEFGHIJ')
        for i in range(len(self._ships)):
            for j in range(len(self._ships[i])):
                if self._ships[i][j] is True:
                    strshipsw[i + 1][j] = 'X'
                elif self._ships[i][j] is False:
                    strshipsw[i + 1][j] = '•'
                elif self._ships[i][j] is None:
                    strshipsw[i + 1][j] = ' '
                else:
                    strshipsw[i + 1][j] = '*'
        for i in range(len(self._ships)):
            strshipsw[i + 1] = ''.join(strshipsw[i + 1])
            if i + 1 < 10:
                strshipsw[i + 1] = ' ' + str(i + 1) + strshipsw[i + 1]
            else:
                strshipsw[i + 1] = str(i + 1) + strshipsw[i + 1]
        strshipsw = '\n'.join(strshipsw)
        return strshipsw


class Game:
    def __init__(self):
        pl1 = input('Player 1, enter your name: ')
        os.system('cls')
        pl2 = input('Player 2, enter your name: ')
        self._field = [Field(), Field()]
        self._players = [Player(pl1), Player(pl2)]
        self._current_player = 0

    def read_position(self):
        pos = Player.read_position()
        return pos

    def field_without_ships(self, ind):
        print(self._field[ind].field_without_ships())

    def field_with_ships(self, ind):
        print(self._field[ind].field_with_ships())

    def shooter(self, pind, fin):
        zil = self._players[pind].read_position()
        ship = self._field[fin].shoot_at(zil)
        if ship != False:            
            leng = ship._length[1] if ship.horizontal else ship._length[0]
           # ship._hit[ship._hit.index(False)] = True
           # print(ship._hit)
            if ship._hit == [True for i in range(leng)]:
                print('\n', ' You DESTROYED the ship!!!')
            else:
                print('\n', ' You damaged the ship!')
            return ship

g = Game()
while True:
    os.system('cls')
    if g._field[g._current_player].counter == 20:
        print(' You won the game! Congratulations!')
    #     winner = g._players[(g._current_player - 1) % 2]._name
    #     print(winner, 'WON!')
        break
    print('\n')
    g.field_with_ships(g._current_player)
    print('\n')
    g.field_without_ships((g._current_player - 1) % 2)
    #print(g._field[g._current_player].di)
#    print(g._field[(g._current_player + 1 )%2].counter)
    if not g.shooter(g._current_player, (g._current_player + 1) % 2):
        input(" Press something to start")
        g._current_player = (g._current_player + 1) % 2
        os.system('cls')
    input(' Press any button ')
