import gamePiece


class rook(gamePiece.gamePiece):
    def __init__(self, color, position, width, height, visible):
        if color == 'white':
            image = "1x/wrook.png"
        else:
            image = "1x/brook.png"
        self.imageFile = image
        super().__init__(color, position, self.imageFile, width, height, visible)

    def getMoves(self, friend, enemy):
        if self.visible:
            cordList = [[], []]

            x = self.position[0]
            y = self.position[1]

            for i in range(8):
                cordList[0].append([x, i])
                cordList[1].append([i, y])

            for piece in friend:
                if piece.position != self.position:

                    for i in range(len(cordList[1])):
                        w = i
                        try:
                            moves = cordList[1][w]
                        except IndexError:
                            w = len(cordList[1]) - 1
                            try:
                                moves = cordList[1][w]
                            except IndexError:
                                break
                        if ((piece.position[0] >= moves[0]) and (piece.position[1] == moves[1])) and (self.position[0] >= piece.position[0]):
                            a, b = piece.position
                            while (a >= moves[0]) and (b == moves[1]):
                                if [a, b] in cordList[1]:
                                    cordList[1].remove([a, b])
                                a -= 1
                        if ((piece.position[0] <= moves[0]) and (piece.position[1] == moves[1])) and (self.position[0] <= piece.position[0]):
                            a, b = piece.position
                            while (a <= moves[0]) and (b == moves[1]):
                                if [a, b] in cordList[1]:
                                    cordList[1].remove([a, b])
                                a += 1
                    for i in range(len(cordList[0])):
                        w = i
                        try:
                            moves = cordList[0][w]
                        except IndexError:
                            w = len(cordList[0]) - 1
                            try:
                                moves = cordList[0][w]
                            except IndexError:
                                break
                        if ((piece.position[0] == moves[0]) and (piece.position[1] >= moves[1])) and (self.position[1] >= piece.position[1]):
                            a, b = piece.position
                            while (a == moves[0]) and (b >= moves[1]):
                                if [a, b] in cordList[0]:
                                    cordList[0].remove([a, b])
                                b -= 1
                        if ((piece.position[0] == moves[0]) and (piece.position[1] <= moves[1])) and (self.position[1] <= piece.position[1]):
                            a, b = piece.position
                            while (a == moves[0]) and (b <= moves[1]):
                                if [a, b] in cordList[0]:
                                    cordList[0].remove([a, b])
                                b += 1


                if piece.position in cordList[0]:
                    cordList[0].remove(piece.position)
                if piece.position in cordList[1]:
                    cordList[1].remove(piece.position)

            # Return the cord List
            return cordList
        else:
            return None

    def setPosition(self, position):
        super().__init__(self.color, position, self.imageFile, self.width, self.height, self.visible)

    def setVisible(self, visible):
        super().__init__(self.color, self.position, self.imageFile, self.width, self.height, visible)
