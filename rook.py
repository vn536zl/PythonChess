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
        cordList = [[], []]

        # logic for getting all the moves in piece row
        limiter = False
        for rows in range(8):
            if limiter:
                break
            row = rows
            if row >= self.position[0]:
                row = -rows
            add_row = self.position[0] + row
            if add_row < 0:
                add_row = -(self.position[0] + row)
            elif add_row > 7:
                add_row = self.position[0] - row
            cordList[0].append([add_row, self.position[1]])

        # logic for getting all the moves in piece column
        limiter = False
        for column in range(8):
            if limiter:
                break
            col = column
            if col >= self.position[1]:
                col = -col
            add_col = self.position[1] + col
            if add_col < 0:
                add_col = -(self.position[1] + col)
            elif add_col > 7:
                add_col = self.position[1] - col
            cordList[1].append([self.position[0], add_col])

        # Return the list of cords

        for i in range(len(friend)):

            #remove position of friends
            if friend[i].position in cordList[0]:
                cordList[0].remove(friend[i].position)
            if friend[i].position in cordList[1]:
                cordList[1].remove(friend[i].position)

            if friend[i].position is not self.position:
                if friend[i].position[0] != 0 and friend[i].position[0] != 1:

                    for x in range(8):
                        if x < friend[i].position[0]:
                            continue
                        else:
                            if [x, friend[i].position[1]] in cordList[0]:
                                cordList[0].remove([x, friend[i].position[1]])
                elif friend[i].position[1] != 0 and friend[i].position[1] != 1:

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