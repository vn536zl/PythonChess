import gamePiece


class rook(gamePiece.gamePiece):
    def __init__(self, color, position, width, height, visible):
        if color == 'white':
            image = "1x/wrook.png"
        else:
            image = "1x/brook.png"
        self.imageFile = image
        super().__init__(color, position, self.imageFile, width, height, visible)

    def getPosableMoves(self, friend, enemy):
        cordList = [[], []]

        # logic for getting all the moves in piece row
        x = self.position[0]
        y = self. position[1]

        a = x
        b = y - 1
        while (7 > a >= 0) and (7 > b >= 0):
            cordList[0].append([a, b])
            try

        # Return the list of cords

        for i in range(len(friend)):

            # remove position of friends/self
            if friend[i].position in cordList[0]:
                cordList[0].remove(friend[i].position)
            if friend[i].position in cordList[1]:
                cordList[1].remove(friend[i].position)

            # Remove possible moves if friend is in the way
            if friend[i].position != self.position:
                if (friend[i].position[0] != 0) and (friend[i].position[0] != 1):

                    for x in range(8):
                        if x < friend[i].position[0]:
                            continue
                        else:
                            if [x, friend[i].position[1]] in cordList[0]:
                                cordList[0].remove([x, friend[i].position[1]])
                elif (friend[i].position[1] != 0) and (friend[i].position[1] != 1):

                    for x in range(8):
                        if x < friend[i].position[1]:
                            continue
                        else:
                            if [friend.position[0], x] in cordList[0]:
                                cordList[0].remove([friend[i].position[0], x])
            else:
                continue

        return cordList

    def setPosition(self, position):
        super().__init__(self.color, position, self.imageFile, self.width, self.height, self.visible)

    def setVisable(self, visible):
        super().__init__(self.color, self.position, self.imageFile, self.width, self.height, visible)
