import random
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
                        ships = [(y, x), (y, x + 1), (y, x + 2), (y, x + 3)]
                        mapa = zanulka(mapa, ships)
                        mapa[y][0] = mapa[y][0][:(x + 1)] + '***' + mapa[y][0][(x + 4):]
                        a = 'Done'
                        mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                        break
                else:
                    break
            elif ran == 1:
                if x > 2:
                    if mapa[y][0][x - 1] == ' ' and mapa[y][0][x - 2] == ' ' and mapa[y][0][x - 3] == ' ':
                        ships = [(y, x), (y, x - 1), (y, x - 2), (y, x - 3)]
                        mapa = zanulka(mapa, ships)
                        mapa[y][0] = mapa[y][0][:(x - 3)] + '***' + mapa[y][0][(x):]
                        a = 'Done'
                        mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                        break
                else:
                    break
            elif ran == 2:
                if y > 2:
                    if mapa[y - 1][0][x] == ' ' and mapa[y - 2][0][x] == ' ' and mapa[y - 3][0][x] == ' ':
                        ships = [(y, x), (y - 1, x), (y - 2, x), (y - 3, x)]
                        mapa = zanulka(mapa, ships)
                        mapa[y - 1][0] = mapa[y - 1][0][:(x)] + '*' + mapa[y - 1][0][(x + 1):]
                        mapa[y - 2][0] = mapa[y - 2][0][:(x)] + '*' + mapa[y - 2][0][(x + 1):]
                        mapa[y - 3][0] = mapa[y - 3][0][:(x)] + '*' + mapa[y - 3][0][(x + 1):]
                        a = 'Done'
                        mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                        break
                else:
                    #                    print('e')
                    break
            elif ran == 3:
                if y < 7:
                    if mapa[y + 1][0][x] == ' ' and mapa[y + 2][0][x] == ' ' and mapa[y + 3][0][x] == ' ':
                        ships = [(y, x), (y + 1, x), (y + 2, x), (y + 3, x)]
                        mapa = zanulka(mapa, ships)
                        mapa[y + 1][0] = mapa[y + 1][0][:(x)] + '*' + mapa[y + 1][0][(x + 1):]
                        mapa[y + 2][0] = mapa[y + 2][0][:(x)] + '*' + mapa[y + 2][0][(x + 1):]
                        mapa[y + 3][0] = mapa[y + 3][0][:(x)] + '*' + mapa[y + 3][0][(x + 1):]
                        a = 'Done'
                        mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
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
                            ships = [(y, x), (y, x + 1), (y, x + 2)]
                            mapa = zanulka(mapa, ships)
                            mapa[y][0] = mapa[y][0][:(x + 1)] + '**' + mapa[y][0][(x + 3):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 1:
                    if x > 1:
                        if mapa[y][0][x - 1] == ' ' and mapa[y][0][x - 2] == ' ' and mapa[y][0][x] == ' ':
                            ships = [(y, x), (y, x - 1), (y, x - 2)]
                            mapa = zanulka(mapa, ships)
                            mapa[y][0] = mapa[y][0][:(x - 2)] + '**' + mapa[y][0][(x):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 2:
                    if y > 1:
                        if mapa[y - 1][0][x] == ' ' and mapa[y - 2][0][x] == ' ' and mapa[y][0][x] == ' ':
                            ships = [(y, x), (y - 1, x), (y - 2, x)]
                            mapa = zanulka(mapa, ships)
                            mapa[y - 1][0] = mapa[y - 1][0][:(x)] + '*' + mapa[y - 1][0][(x + 1):]
                            mapa[y - 2][0] = mapa[y - 2][0][:(x)] + '*' + mapa[y - 2][0][(x + 1):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 3:
                    if y < 8:
                        if mapa[y + 1][0][x] == ' ' and mapa[y + 2][0][x] == ' ' and mapa[y][0][x] == ' ':
                            ships = [(y, x), (y + 1, x), (y + 2, x)]
                            mapa = zanulka(mapa, ships)
                            mapa[y + 1][0] = mapa[y + 1][0][:(x)] + '*' + mapa[y + 1][0][(x + 1):]
                            mapa[y + 2][0] = mapa[y + 2][0][:(x)] + '*' + mapa[y + 2][0][(x + 1):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
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
                            ships = [(y, x), (y, x + 1)]
                            mapa = zanulka(mapa, ships)
                            mapa[y][0] = mapa[y][0][:(x + 1)] + '*' + mapa[y][0][(x + 2):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 1:
                    if x > 0:
                        if mapa[y][0][x] == ' ' and mapa[y][0][x - 1] == ' ':
                            ships = [(y, x), (y, x - 1)]
                            mapa = zanulka(mapa, ships)
                            mapa[y][0] = mapa[y][0][:(x - 1)] + '**' + mapa[y][0][(x + 1):]
                            a = 'Done'
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 2:
                    if y > 0:
                        if mapa[y - 1][0][x] == ' ' and mapa[y][0][x] == ' ':
                            ships = [(y - 1, x), (y, x)]
                            mapa = zanulka(mapa, ships)
                            mapa[y - 1][0] = mapa[y - 1][0][:(x)] + '*' + mapa[y - 1][0][(x + 1):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            break
                    else:
                        #                        print('e')
                        break
                elif ran == 3:
                    if y < 9:
                        if mapa[y + 1][0][x] == ' ' and mapa[y][0][x] == ' ':
                            ships = [(y + 1, x), (y, x)]
                            mapa = zanulka(mapa, ships)
                            mapa[y + 1][0] = mapa[y + 1][0][:(x)] + '*' + mapa[y + 1][0][(x + 1):]
                            a = 'Done'
                            mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
                            break
                    else:
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
            if mapa[y][0][x] == ' ':
                ships = [(y, x)]
                mapa = zanulka(mapa, ships)
                zanulka(mapa, ships)
                a = 'Done'
                mapa[y][0] = mapa[y][0][:x] + '*' + mapa[y][0][(x + 1):]
    return mapa


def zanulka(mapa, points):
    for i in points:
        if i[0] < 9 and i[1] < 9 and i[0] > 0 and i[1] > 0:
            if mapa[i[0] + 1][0][i[1]] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1]] + '•' + mapa[i[0] + 1][0][i[1] + 1:]
            if mapa[i[0] + 1][0][i[1] - 1] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1] - 1] + '•' + mapa[i[0] + 1][0][i[1]:]
            if mapa[i[0] + 1][0][i[1] + 1] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1] + 1] + '•' + mapa[i[0] + 1][0][i[1] + 2:]
            if mapa[i[0] - 1][0][i[1]] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1]] + '•' + mapa[i[0] - 1][0][i[1] + 1:]
            if mapa[i[0] - 1][0][i[1] - 1] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1] - 1] + '•' + mapa[i[0] - 1][0][i[1]:]
            if mapa[i[0] - 1][0][i[1] + 1] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1] + 1] + '•' + mapa[i[0] - 1][0][i[1] + 2:]
            if mapa[i[0]][0][i[1] - 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] - 1] + '•' + mapa[i[0]][0][i[1]:]
            if mapa[i[0]][0][i[1] + 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] + 1] + '•' + mapa[i[0]][0][i[1] + 2:]
        elif i[0] == 0 and i[1] > 0 and i[1] < 9:
            if mapa[i[0] + 1][0][i[1]] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1]] + '•' + mapa[i[0] + 1][0][i[1] + 1:]
            if mapa[i[0] + 1][0][i[1] - 1] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1] - 1] + '•' + mapa[i[0] + 1][0][i[1]:]
            if mapa[i[0] + 1][0][i[1] + 1] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1] + 1] + '•' + mapa[i[0] + 1][0][i[1] + 2:]
            if mapa[i[0]][0][i[1] - 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] - 1] + '•' + mapa[i[0]][0][i[1]:]
            if mapa[i[0]][0][i[1] + 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] + 1] + '•' + mapa[i[0]][0][i[1] + 2:]
        elif i[0] == 9 and i[1] > 0 and i[1] < 9:
            if mapa[i[0]][0][i[1] - 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] - 1] + '•' + mapa[i[0]][0][i[1]:]
            if mapa[i[0]][0][i[1] + 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] + 1] + '•' + mapa[i[0]][0][i[1] + 2:]
            if mapa[i[0] - 1][0][i[1]] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1]] + '•' + mapa[i[0] - 1][0][i[1] + 1:]
            if mapa[i[0] - 1][0][i[1] - 1] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1] - 1] + '•' + mapa[i[0] - 1][0][i[1]:]
            if mapa[i[0] - 1][0][i[1] + 1] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1] + 1] + '•' + mapa[i[0] - 1][0][i[1] + 2:]
        elif i[0] > 0 and i[0] < 9 and i[1] == 0:
            if mapa[i[0] + 1][0][i[1]] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1]] + '•' + mapa[i[0] + 1][0][i[1] + 1:]
            if mapa[i[0] + 1][0][i[1] + 1] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1] + 1] + '•' + mapa[i[0] + 1][0][i[1] + 2:]
            if mapa[i[0] - 1][0][i[1]] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1]] + '•' + mapa[i[0] - 1][0][i[1] + 1:]
            if mapa[i[0] - 1][0][i[1] + 1] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1] + 1] + '•' + mapa[i[0] - 1][0][i[1] + 2:]
            if mapa[i[0]][0][i[1] + 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] + 1] + '•' + mapa[i[0]][0][i[1] + 2:]
        elif i[0] > 0 and i[0] < 9 and i[1] == 9:
            if mapa[i[0] + 1][0][i[1]] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1]] + '•' + mapa[i[0] + 1][0][i[1] + 1:]
            if mapa[i[0] + 1][0][i[1] - 1] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1] - 1] + '•' + mapa[i[0] + 1][0][i[1]:]
            if mapa[i[0] - 1][0][i[1]] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1]] + '•' + mapa[i[0] - 1][0][i[1] + 1:]
            if mapa[i[0] - 1][0][i[1] - 1] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1] - 1] + '•' + mapa[i[0] - 1][0][i[1]:]
            if mapa[i[0]][0][i[1] - 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] - 1] + '•' + mapa[i[0]][0][i[1]:]
        elif i[0] == 0 and i[1] == 0:
            if mapa[i[0] + 1][0][i[1]] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1]] + '•' + mapa[i[0] + 1][0][i[1] + 1:]
            if mapa[i[0] + 1][0][i[1] + 1] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1] + 1] + '•' + mapa[i[0] + 1][0][i[1] + 2:]
            if mapa[i[0]][0][i[1] + 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] + 1] + '•' + mapa[i[0]][0][i[1] + 2:]
        elif i[0] == 0 and i[1] == 9:
            if mapa[i[0] + 1][0][i[1]] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1]] + '•' + mapa[i[0] + 1][0][i[1] + 1:]
            if mapa[i[0] + 1][0][i[1] - 1] == ' ':
                mapa[i[0] + 1][0] = mapa[i[0] + 1][0][:i[1] - 1] + '•' + mapa[i[0] + 1][0][i[1]:]
            if mapa[i[0]][0][i[1] - 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] - 1] + '•' + mapa[i[0]][0][i[1]:]
        elif i[0] == 9 and i[1] == 0:
            if mapa[i[0]][0][i[1] + 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] + 1] + '•' + mapa[i[0]][0][i[1] + 2:]
            if mapa[i[0] - 1][0][i[1]] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1]] + '•' + mapa[i[0] - 1][0][i[1] + 1:]
            if mapa[i[0] - 1][0][i[1] + 1] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1] + 1] + '•' + mapa[i[0] - 1][0][i[1] + 2:]
        elif i[0] == 9 and i[1] == 9:
            if mapa[i[0]][0][i[1] - 1] == ' ':
                mapa[i[0]][0] = mapa[i[0]][0][:i[1] - 1] + '•' + mapa[i[0]][0][i[1]:]
            if mapa[i[0] - 1][0][i[1]] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1]] + '•' + mapa[i[0] - 1][0][i[1] + 1:]
            if mapa[i[0] - 1][0][i[1] - 1] == ' ':
                mapa[i[0] - 1][0] = mapa[i[0] - 1][0][:i[1] - 1] + '•' + mapa[i[0] - 1][0][i[1]:]
    return mapa
