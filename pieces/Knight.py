import pieces.GamePiece


class Knight(pieces.GamePiece.GamePiece):
    def __init__(self, color, position, visible):
        if (color == 'white'):
            self.imageFile = "pieces/images/wknight.png"
        elif (color == 'black'):
            self.imageFile = "pieces/images/bknight.png"
        self.moves = 0
        self.name = type(self).__name__
        self.id = type(self).__name__ + str(position[0]) + str(position[1])
        super().__init__(self.imageFile, color, position, visible, self.moves)

    def getMoves(self):
        # Get all possiable moves for piece
        moveList = []
        for y in range(8):
            for x in range(8):
                move = (x, y)
                if (move == (self.position[0] + 2, self.position[1] + 1)):
                    moveList.append((x, y))
                elif (move == (self.position[0] - 2, self.position[1] + 1)):
                    moveList.append((x, y))
                elif (move == (self.position[0] + 2, self.position[1] - 1)):
                    moveList.append((x, y))
                elif (move == (self.position[0] - 2, self.position[1] - 1)):
                    moveList.append((x, y))
                elif (move == (self.position[0] + 1, self.position[1] + 2)):
                    moveList.append((x, y))
                elif (move == (self.position[0] - 1, self.position[1] + 2)):
                    moveList.append((x, y))
                elif (move == (self.position[0] + 1, self.position[1] - 2)):
                    moveList.append((x, y))
                elif (move == (self.position[0] - 1, self.position[1] - 2)):
                    moveList.append((x, y))

        # Remove piece position from list
        if (self.position in moveList):
            moveList.remove(self.position)

        # remove other pieces position from list
        for piece in self.all_pieces:
            if ((piece.position in moveList) and (piece.color == self.color)):
                moveList.remove(piece.position)

        return moveList
