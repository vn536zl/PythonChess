import pieces.GamePiece


class Rook(pieces.GamePiece.GamePiece):
    def __init__(self, color, position, visible):
        if (color == 'white'):
            self.imageFile = "pieces/images/wrook.png"
        elif (color == 'black'):
            self.imageFile = "pieces/images/brook.png"
        self.moves = 0
        super().__init__(self.imageFile, color, position, visible, self.moves)

    def getMoves(self):
        # Get all possiable moves for piece
        moveList = []
        for y in range(8):
            for x in range(8):

                if (x == self.position[0]):
                    moveList.append((x, y))
                elif (y == self.position[1]):
                    moveList.append((x, y))

        # Remove piece position from list
        if (self.position in moveList):
            moveList.remove(self.position)

        # remove other pieces position from list
        for piece in self.all_pieces:

            if ((piece.position in moveList) and (piece.color == self.color)):
                moveList.remove(piece.position)

            pieceX = piece.position[0]
            pieceY = piece.position[1]

            # Remove X positions where another piece is in the way
            if ((piece.position[0] > self.position[0]) and (pieceY == self.position[1])):
                while (piece.position[0] <= pieceX <= 7):
                    pieceX += 1
                    if ((pieceX, self.position[1]) in moveList):
                        moveList.remove((pieceX, self.position[1]))
            if ((piece.position[0] < self.position[0]) and (pieceY == self.position[1])):
                while (piece.position[0] >= pieceX >= 0):
                    pieceX -= 1
                    if ((pieceX, self.position[1]) in moveList):
                        moveList.remove((pieceX, self.position[1]))

            # Remove Y positions where another piece is in the way
            if ((piece.position[1] > self.position[1]) and (pieceX == self.position[0])):
                while (piece.position[1] <= pieceY <= 7):
                    pieceY += 1
                    if ((self.position[0], pieceY) in moveList):
                        moveList.remove((self.position[0], pieceY))
            if ((piece.position[1] < self.position[1]) and (pieceX == self.position[0])):
                while (piece.position[1] >= pieceY >= 0):
                    pieceY -= 1
                    if ((self.position[0], pieceY) in moveList):
                        moveList.remove((self.position[0], pieceY))

        return moveList
