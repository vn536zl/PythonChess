import gamePiece


class bishop(gamePiece.gamePiece):
    def __init__(self, color, position, width, height, visible):
        if color == 'white':
            image = "1x/wbishop.png"
        else:
            image = "1x/bbishop.png"
        self.imageFile = image
        super().__init__(color, position, self.imageFile, width, height, visible)

    def getMoves(self, friend, enemy):
        if self.visible:
            cordList = [[], []]
            rows = []
            cols = []

            # logic for getting all the moves in piece row
            x = self.position[0]
            y = self.position[1]

            # Up Right
            a = x + 1
            b = y - 1
            while (7 >= a >= 0) and (7 >= b >= 0):
                cols.append([a, b])
                try:
                    cols.append([a + 1, b - 1])
                except IndexError:
                    pass
                b -= 1
                a += 1

            # Down Right
            a = x + 1
            b = y + 1
            while (7 >= a >= 0) and (7 >= b >= 0):
                cols.append([a, b])
                try:
                    cols.append([a + 1, b + 1])
                except IndexError:
                    pass
                b += 1
                a += 1

            # Down Left
            a = x - 1
            b = y + 1
            while (7 >= a >= 0) and (7 >= b >= 0):
                rows.append([a, b])
                try:
                    rows.append([a - 1, b + 1])
                except IndexError:
                    pass
                a -= 1
                b += 1

            #  Up Left
            a = x - 1
            b = y - 1
            while (7 >= a >= 0) and (7 >= b >= 0):
                rows.append([a, b])
                try:
                    rows.append([a - 1, b - 1])
                except IndexError:
                    pass
                a -= 1
                b -= 1

            # Remove duplicates
            for i in rows:
                if i not in cordList[0]:
                    cordList[0].append(i)
            for i in cols:
                if i not in cordList[1]:
                    cordList[1].append(i)

            for i in cordList[0]:
                if (i[0] < 0) or (i[1] < 0):
                    cordList[0].remove(i)
                if (i[0] >= 8) or (i[1] >= 8):
                    cordList[0].remove(i)
            for i in cordList[1]:
                if (i[0] < 0) or (i[1] < 0):
                    cordList[1].remove(i)
                if (i[0] >= 8) or (i[1] >= 8):
                    cordList[1].remove(i)

            for i in range(len(friend)):

                # remove position of friends/self
                if friend[i].position in cordList[0]:
                    cordList[0].remove(friend[i].position)
                if friend[i].position in cordList[1]:
                    cordList[1].remove(friend[i].position)

                # Remove possible moves if friend is in the way
                if friend[i].position != self.position:
                    x = friend[i].position[0]
                    y = friend[i].position[1]

                    if (x != 0) and (x != 1):

                        if self.position[0] < x:
                            for k in range(8):
                                if k < x:
                                    continue
                                elif [k, y] in cordList[0]:
                                    cordList[0].remove([k, y])
                        elif self.position[0] > x:
                            for k in range(8):
                                if k > x:
                                    continue
                                elif [k, y] in cordList[0]:
                                    cordList[0].remove([k, y])

                    if (y != 0) and (y != 1):

                        if self.position[1] < y:
                            for k in range(8):
                                if k < y:
                                    continue
                                elif [x, k] in cordList[1]:
                                    cordList[1].remove([x, k])
                        if self.position[1] > y:
                            for k in range(8):
                                if k > y:
                                    continue
                                elif [x, k] in cordList[1]:
                                    cordList[1].remove([x, k])

            for i in range(len(enemy)):

                x = enemy[i].position[0]
                y = enemy[i].position[1]

                if (x != 0) and (x != 1):

                    if self.position[0] < x:
                        for k in range(8):
                            if [k, y] != [x, y]:
                                if k < x:
                                    continue
                                elif [k, y] in cordList[0]:
                                    cordList[0].remove([k, y])
                    elif self.position[0] > x:
                        for k in range(8):
                            if [k, y] != [x, y]:
                                if k < x:
                                    continue
                                elif [k, y] in cordList[0]:
                                    cordList[0].remove([k, y])

                if (y != 0) and (y != 1):

                    if self.position[1] < y:
                        for k in range(8):
                            if [x, k] != [x, y]:
                                if k < y:
                                    continue
                                elif [x, k] in cordList[1]:
                                    cordList[1].remove([x, k])
                    if self.position[1] > y:
                        for k in range(8):
                            if [x, k] != [x, y]:
                                if k < y:
                                    continue
                                elif [x, k] in cordList[1]:
                                    cordList[1].remove([x, k])

            return cordList
        else:
            return None

    def setPosition(self, position):
        super().__init__(self.color, position, self.imageFile, self.width, self.height, self.visible)

    def setVisible(self, visible):
        super().__init__(self.color, self.position, self.imageFile, self.width, self.height, visible)