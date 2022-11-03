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
            run = True
            a = x + 1
            b = y - 1
            while ((7 >= a >= 0) and (7 >= b >= 0)) and run:
                cols.append([a, b])
                try:
                    for piece in friend:
                        if (piece.position[0] >= (a + 1) and piece.position[1] >= (b - 1)) and piece.position != self.position:
                            run = False
                            break
                        else:
                            cols.append([a, b])
                    for piece in enemy:
                        if piece.position[0] <= (a + 1) and piece.position[1] <= (b - 1):
                            run = False
                            break
                        else:
                            cols.append([a, b])
                except IndexError:
                    pass
                b -= 1
                a += 1

            # Down Right
            run = True
            a = x + 1
            b = y + 1
            while ((7 >= a >= 0) and (7 >= b >= 0)) and run:
                cols.append([a, b])
                try:
                    for piece in friend:
                        if (piece.position[0] >= (a + 1) and piece.position[1] >= (b + 1)) and piece.position != self.position:
                            run = False
                            break
                        else:
                            cols.append([a, b])
                    for piece in enemy:
                        if piece.position[0] <= (a + 1) and piece.position[1] <= (b + 1):
                            run = False
                            break
                        else:
                            cols.append([a, b])
                except IndexError:
                    pass
                b += 1
                a += 1

            # Down Left
            run = True
            a = x - 1
            b = y + 1
            while ((7 >= a >= 0) and (7 >= b >= 0)) and run:
                rows.append([a, b])
                try:
                    for piece in friend:
                        if (piece.position[0] <= (a - 1) and piece.position[1] >= (b + 1)) and piece.position != self.position:
                            run = False
                            break
                        else:
                            rows.append([a, b])
                    for piece in enemy:
                        if piece.position[0] >= (a - 1) and piece.position[1] <= (b + 1):
                            run = False
                            break
                        else:
                            rows.append([a, b])
                except IndexError:
                    pass
                a -= 1
                b += 1

            #  Up Left
            run = True
            a = x - 1
            b = y - 1
            while ((7 >= a >= 0) and (7 >= b >= 0)) and run:
                rows.append([a, b])
                try:
                    for piece in friend:
                        if (piece.position[0] <= (a - 1) and piece.position[1] <= (b - 1)) and piece.position != self.position:
                            run = False
                            break
                        else:
                            rows.append([a, b])
                    for piece in enemy:
                        if piece.position[0] >= (a - 1) and piece.position[1] >= (b - 1):
                            run = False
                            break
                        else:
                            rows.append([a, b])
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

############# Friend list Beginning #########################

            for i in range(len(friend)):

                # remove position of friends/self
                if friend[i].position in cordList[0]:
                    cordList[0].remove(friend[i].position)
                if friend[i].position in cordList[1]:
                    cordList[1].remove(friend[i].position)

############## Friend list ending ###########################

            return cordList
        else:
            return None

    def setPosition(self, position):
        super().__init__(self.color, position, self.imageFile, self.width, self.height, self.visible)

    def setVisible(self, visible):
        super().__init__(self.color, self.position, self.imageFile, self.width, self.height, visible)