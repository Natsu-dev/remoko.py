def showField(l, fieldStr):
    field = ""
    fieldStr = ""
    for n in l:
        if n == 0:
            field += '⬛'
        elif n == 1:
            field += '🔵'
        elif n == 2:
            field += '⚪'

    fieldStr += '🈁1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣🈁\n'
    fieldStr += '1️⃣{}🈁\n'.format(field[0:8])
    fieldStr += '2️⃣{}🈁\n'.format(field[8:16])
    fieldStr += '3️⃣{}🈁\n'.format(field[16:24])
    fieldStr += '4️⃣{}🈁\n'.format(field[24:32])
    fieldStr += '5️⃣{}🈁\n'.format(field[32:40])
    fieldStr += '6️⃣{}🈁\n'.format(field[40:48])
    fieldStr += '7️⃣{}🈁\n'.format(field[48:56])
    fieldStr += '8️⃣{}🈁\n'.format(field[56:64])
    fieldStr += '🈁🈁🈁🈁🈁🈁🈁🈁🈁🈁'
    return fieldStr


def playReversi(turn):
    print('start playing reversi.')
    fieldStr = ""
    fieldInt = [0] * 64
    fieldInt[27] = 1
    fieldInt[28] = 2
    fieldInt[36] = 1
    fieldInt[35] = 2

    return showField(fieldInt, fieldStr)
