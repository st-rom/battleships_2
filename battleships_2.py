import random


# read_field('C:/Users/voyo/Documents/Python Codes/Feb/filename.txt')
def read_field(filename):
    '''
    (str) -> (data)
    >>> read_field('filename.txt')
    [['  ***     '], ['**  **  **'], ['  **** ***'], ['     *    '],
    ['   *      '], ['         *'], ['          '], ['          '],
    ['         *'], ['          ']]
    '''
    mapa = []
    with open(filename) as f:
        for i in f:
            i = i.split('\n')
            mapa.append(i)
        for j in range(len(mapa)):
            if len(mapa[j]) == 2:
                mapa[j].remove(mapa[j][-1])
    return mapa


def has_ship(mapa, target):
    '''
    (data, tuple) -> (bool)
    >>> has_ship(read_field(), ('J', 10))
    False
    >>> has_ship(read_field(), ('E', 2))
    True
    '''
    if mapa[int(target[-1]) - 1][0][ord(target[0]) - 65] == ' ':
        return False
    else:
        return True


# ship_size(read_field('C:/Users/voyo/Documents/Python Codes/Feb/filename.txt'), ('J', 2))
def ship_size(mapa, target):
    '''
    (data, tuple) -> (tuple)
    >>> ship_size(read_field(filename.txt'), ('J', 2))
    (3, 1)
    >>> ship_size(read_field(filename.txt'), ('B', 5))
    (1, 2)
    '''
    if mapa[int(target[-1]) - 1][0][ord(target[0]) - 65] == ' ':
        return 'There is no ship'
    else:
        i = 1
        j = 1
        l = 1
        y = 1
        ship_l = 1
        xy = 'x'
        while True:
            try:
                if mapa[int(target[-1]) - 1 - i][0][ord(target[0]) - 65] == '*' or mapa[int(target[-1]) - 1 - i][0][
                            ord(target[0]) - 65] == 'X':
                    i += 1
                    ship_l += 1
                    xy = 'y'
                elif mapa[int(target[-1]) - 1 + j][0][ord(target[0]) - 65] == '*' or mapa[int(target[-1]) - 1 + j][0][
                            ord(target[0]) - 65] == 'X':
                    j += 1
                    ship_l += 1
                    xy = 'y'
                elif mapa[int(target[-1]) - 1][0][ord(target[0]) - 65 - l] == '*' or mapa[int(target[-1]) - 1][0][
                                    ord(target[0]) - 65 - l] == 'X':
                    l += 1
                    ship_l += 1
                    xy = 'x'
                elif mapa[int(target[-1]) - 1][0][ord(target[0]) - 65 + y] == '*' or mapa[int(target[-1]) - 1][0][
                                    ord(target[0]) - 65 + y] == 'X':
                    y += 1
                    ship_l += 1
                    xy = 'x'
                else:
                    break
            except:
                break
        if xy == 'x':
            return ship_l, 1
        elif xy == 'y':
            return 1, ship_l


# check(read_field('C:/Users/voyo/Documents/Python Codes/Feb/filename.txt'), ('J', 2))
def check(mapa, target):
    mapa[int(target[-1]) - 1][0] = mapa[int(target[-1]) - 1][0][:(ord(target[0]) - 65)] + 'X' + \
                                   mapa[int(target[-1]) - 1][0][(ord(target[0]) - 65 + 1):]
    print('  ABCDEFGHIJ')
    let = 0
    for i in mapa:
        for j in i:
            let += 1
            if let < 10:
                print('', let, j)
            else:
                print(let, j)


# field_to_str(read_field('C:/Users/voyo/Documents/Python Codes/Feb/filename.txt'))
def field_to_str(mapa):
    '''
    (mapa) -> (str)
    '''
    print('  ABCDEFGHIJ')
    let = 0
    for i in mapa:
        for j in i:
            let += 1
            if let < 10:
                print('', let, j)
            else:
                print(let, j)
    con = input(" If you want to write this to the file type 'yes'\n ")
    if con == 'yes':
        writing_f(mapa)


def writing_f(mapa):
    file = open('C:/Users/voyo/Documents/Python Codes/Feb/filename1.txt', 'w')
    for i in mapa:
        for j in i:
            file.write(j + '\n')


# is_valid(read_field('C:/Users/voyo/Documents/Python Codes/Feb/filename.txt'))
def is_valid(mapa):
    '''
    (data) -> (bool)
    >>> is_valid(read_field('filename.txt'))
    True
    >>> is_valid(read_field('filename.txt'))
    False
    '''
    jour = {'1-sized': 0, '2-sized': 0, '3-sized': 0, '4-sized': 0}
    counter = 0
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            if mapa[i][0][j] == '*' or mapa[i][0][j] == 'X':
                mapa[i][0] = mapa[i][0][:j] + '0' + mapa[i][0][(j + 1):]
                counter += 1
                a = b = c = d = size = 1
                while True:
                    try:
                        if (mapa[i - a][0][j] == '*' or mapa[i - a][0][j] == 'X') and (i - a != -1):
                            mapa[i - a][0] = mapa[i - a][0][:j] + '0' + mapa[i - a][0][(j + 1):]
                            counter += 1
                            a += 1
                            size += 1
                        elif mapa[i + b][0][j] == '*' or mapa[i + b][0][j] == 'X':
                            mapa[i + b][0] = mapa[i + b][0][:j] + '0' + mapa[i + b][0][(j + 1):]
                            counter += 1
                            b += 1
                            size += 1
                        elif (mapa[i][0][j - c] == '*' or mapa[i][0][j - c] == 'X') and (j - c != -1):
                            mapa[i][0] = mapa[i][0][:(j - c)] + '0' + mapa[i][0][(j - c + 1):]
                            counter += 1
                            c += 1
                            size += 1
                        elif mapa[i][0][j + d] == '*' or mapa[i][0][j + d] == 'X':
                            mapa[i][0] = mapa[i][0][:(j + d)] + '0' + mapa[i][0][(j + d + 1):]
                            counter += 1
                            d += 1
                            size += 1
                        else:
                            for ii in jour:
                                if ii[0] == str(size):
                                    jour[ii] += 1
                                    break
                            break
                    except:
                        # for jj in jour:
                        #     if jj[0] == str(size):
                        #         jour[jj] += 1
                        #         break
                        break
    print(counter)
    if jour['1-sized'] == 4 and jour['2-sized'] == 3 and \
                    jour['3-sized'] == 2 and jour['4-sized'] == 1 and counter == 20:
        return True
    else:
        return False


def generate_field():
    mapa = [[' ' * 10], [' ' * 10], [' ' * 10], [' ' * 10], [' ' * 10], [' ' * 10], [' ' * 10], [' ' * 10], [' ' * 10],
            [' ' * 10]]
    a = 'nope'
    ships = []
    while a != 'Done':
        ran = random.randrange(4)
        x = random.randrange(10)
        y = random.randrange(10)
        times = 4
        while times != 0:
            if ran == 0:
                if x < 7:
                    if mapa[y][0][x + 1] == ' ' and mapa[y][0][x + 2] == ' ' and mapa[y][0][x + 3] == ' ':
                        mapa[y][0] = mapa[y][0][:(x + 1)] + '***' + mapa[y][0][(x + 4):]
                        a = 'Done'
                        mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                        ships.extend([(y, x), (y, x + 1), (y, x + 2), (y, x + 3)])
                        break
                else:
                    break
            elif ran == 1:
                if x > 2:
                    if mapa[y][0][x - 1] == ' ' and mapa[y][0][x - 2] == ' ' and mapa[y][0][x - 3] == ' ':
                        mapa[y][0] = mapa[y][0][:(x - 3)] + '***' + mapa[y][0][(x):]
                        a = 'Done'
                        mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                        ships.extend([(y, x), (y, x - 1), (y, x - 2), (y, x - 3)])
                        break
                else:
                    break
            elif ran == 2:
                if y > 2:
                    if mapa[y - 1][0][x] == ' ' and mapa[y - 2][0][x] == ' ' and mapa[y - 3][0][x] == ' ':
                        mapa[y - 1][0] = mapa[y - 1][0][:(x)] + '*' + mapa[y - 1][0][(x + 1):]
                        mapa[y - 2][0] = mapa[y - 2][0][:(x)] + '*' + mapa[y - 2][0][(x + 1):]
                        mapa[y - 3][0] = mapa[y - 3][0][:(x)] + '*' + mapa[y - 3][0][(x + 1):]
                        a = 'Done'
                        mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                        ships.extend([(y, x), (y - 1, x), (y - 2, x), (y - 3, x)])
                        #                        print('c', x, y)
                        break
                else:
                    #                    print('e')
                    break
            elif ran == 3:
                if y < 7:
                    if mapa[y + 1][0][x] == ' ' and mapa[y + 2][0][x] == ' ' and mapa[y + 3][0][x] == ' ':
                        mapa[y + 1][0] = mapa[y + 1][0][:(x)] + '*' + mapa[y + 1][0][(x + 1):]
                        mapa[y + 2][0] = mapa[y + 2][0][:(x)] + '*' + mapa[y + 2][0][(x + 1):]
                        mapa[y + 3][0] = mapa[y + 3][0][:(x)] + '*' + mapa[y + 3][0][(x + 1):]
                        a = 'Done'
                        mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                        ships.extend([(y, x), (y + 1, x), (y + 2, x), (y + 3, x)])
                        #                        print('d', x, y)
                        break
                else:
                    #                    print('e')
                    break
            ran += 1
            times -= 1
            if ran == 4:
                ran = 0
    for i in range(2):
        a = 'nope'
        while a != 'Done':
            ran = random.randrange(4)
            x = random.randrange(10)
            y = random.randrange(10)
            times = 4
            #           print(x, y)
            while times != 0:
                #               print(times)
                if ran == 0:
                    if x < 8:
                        if mapa[y][0][x + 1] == ' ' and mapa[y][0][x + 2] == ' ' and mapa[y][0][x] == ' ':
                            mapa[y][0] = mapa[y][0][:(x + 1)] + '**' + mapa[y][0][(x + 3):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            ships.extend([(y, x), (y, x + 1), (y, x + 2)])
                            #                            print('a', x, y)
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 1:
                    if x > 1:
                        if mapa[y][0][x - 1] == ' ' and mapa[y][0][x - 2] == ' ' and mapa[y][0][x] == ' ':
                            mapa[y][0] = mapa[y][0][:(x - 2)] + '**' + mapa[y][0][(x):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            ships.extend([(y, x), (y, x - 1), (y, x - 2)])
                            #                            print('b', x, y)
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 2:
                    if y > 1:
                        if mapa[y - 1][0][x] == ' ' and mapa[y - 2][0][x] == ' ' and mapa[y][0][x] == ' ':
                            mapa[y - 1][0] = mapa[y - 1][0][:(x)] + '*' + mapa[y - 1][0][(x + 1):]
                            mapa[y - 2][0] = mapa[y - 2][0][:(x)] + '*' + mapa[y - 2][0][(x + 1):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            ships.extend([(y, x), (y - 1, x), (y - 2, x)])
                            #                            print('c', x, y)
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 3:
                    if y < 8:
                        if mapa[y + 1][0][x] == ' ' and mapa[y + 2][0][x] == ' ' and mapa[y][0][x] == ' ':
                            mapa[y + 1][0] = mapa[y + 1][0][:(x)] + '*' + mapa[y + 1][0][(x + 1):]
                            mapa[y + 2][0] = mapa[y + 2][0][:(x)] + '*' + mapa[y + 2][0][(x + 1):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            ships.extend([(y, x), (y + 1, x), (y + 2, x)])
                            #                            print('d', x, y)
                            break
                    else:
                        #                        print('e')
                        break
                ran += 1
                times -= 1
                if ran == 4:
                    ran = 0
                    #
    for i in range(3):
        a = 'nope'
        while a != 'Done':
            ran = random.randrange(4)
            x = random.randrange(10)
            y = random.randrange(10)
            times = 4
            #            print(x, y)
            while times != 0:
                #                print(times)
                if ran == 0:
                    if x < 9:
                        if mapa[y][0][x + 1] == ' ' and mapa[y][0][x] == ' ':
                            mapa[y][0] = mapa[y][0][:(x + 1)] + '*' + mapa[y][0][(x + 2):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            #                            print('a', x, y)
                            ships.extend([(y, x), (y, x + 1)])
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 1:
                    if x > 0:
                        if mapa[y][0][x] == ' ' and mapa[y][0][x - 1] == ' ':
                            mapa[y][0] = mapa[y][0][:(x - 1)] + '**' + mapa[y][0][(x + 1):]
                            a = 'Done'
                            ships.extend([(y, x), (y, x - 1)])
                            #                            print('b', x, y)
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 2:
                    if y > 0:
                        if mapa[y - 1][0][x] == ' ' and mapa[y][0][x] == ' ':
                            mapa[y - 1][0] = mapa[y - 1][0][:(x)] + '*' + mapa[y - 1][0][(x + 1):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            #                            print('c', x, y)
                            ships.extend([(y - 1, x), (y, x)])
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 3:
                    if y < 9:
                        if mapa[y + 1][0][x] == ' ' and mapa[y][0][x] == ' ':
                            mapa[y + 1][0] = mapa[y + 1][0][:(x)] + '*' + mapa[y + 1][0][(x + 1):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            ships.extend([(y + 1, x), (y, x)])
                            #                            print('d', x, y)
                            break
                    else:
                        #                        print('e')
                        break
                ran += 1
                times -= 1
                if ran == 4:
                    ran = 0
    for i in range(4):
        a = 'nope'
        while a != 'Done':
            x = random.randrange(10)
            y = random.randrange(10)
            #            print(x, y)
            if mapa[y][0][x] == ' ':
                ships.extend([(y, x)])
                zanulka(mapa, ships)
                a = 'Done'
                mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]

                #                print('a', x, y)
    print(mapa, '\n', ships)
    print(is_valid(mapa))
    return field_to_str(mapa)


def zanulka(mapa, points):
    print(points)
    '''if y > 0:
        if mapa[y - 1][0][x - 1] == ' ':
            mapa[y - 1][0] = mapa[y - 1][0][:(x - 1)] + '*' + mapa[y - 1][0][(x):]
        else:
            stan = '-'
        if mapa[y - 1][0][x - 1] == ' ':
            mapa[y - 1][0] = mapa[y - 1][0][:(x - 1)] + '*' + mapa[y - 1][0][(x):]
        else:
            stan = '-'
       '''


generate_field()