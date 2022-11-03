import pieces.GamePiece


class Pawn(pieces.GamePiece.GamePiece):
    def __init__(self, color, position, visible):
        if (color == 'white'):
            self.imageFile = "pieces/images/wpawn.png"
        elif (color == 'black'):
            self.imageFile = "pieces/images/bpawn.png"
        self.moves = 0
        self.name = type(self).__name__
        super().__init__(self.imageFile, color, position, visible, self.moves)

    def getMoves(self):
        # Get all possiable moves for piece
        moveList = []
        for y in range(8):
            for x in range(8):
                if (self.color == 'black'):
                    if (self.moves > 0):
                        if ((x == self.position[0]) and (y == self.position[1] + 1)):
                            moveList.append((x, y))
                    else:
                        if ((x == self.position[0]) and ((y == self.position[1] + 1) or (y == self.position[1] + 2))):
                            moveList.append((x, y))
                else:
                    if (self.moves > 0):
                        if ((x == self.position[0]) and (y == self.position[1] - 1)):
                            moveList.append((x, y))
                    else:
                        if ((x == self.position[0]) and ((y == self.position[1] - 1) or (y == self.position[1] - 2))):
                            moveList.append((x, y))

        # Remove piece position from list
        if (self.position in moveList):
            moveList.remove(self.position)

        # remove other pieces position from list
        for piece in self.all_pieces:

            if (piece.position in moveList):
                moveList.remove(piece.position)

            pieceX = piece.position[0]
            pieceY = piece.position[1]

            if ((type(piece).__name__ == type(self).__name__) and (piece.color != self.color) and (piece.moves == 1)):
                if ((pieceX == self.position[0]+1 or pieceX == self.position[0]-1) and (pieceY == self.position[1]+1 or pieceY == self.position[1]-1)):
                    moveList.append((pieceX, pieceY))

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

            # Add capturing
            if ((self.color == 'black') and (self.color != piece.color)):
                if ((piece.position[1] == self.position[1] + 1) and (
                        piece.position[0] == self.position[0] + 1 or piece.position[0] == self.position[0] - 1)):
                    moveList.append((pieceX, pieceY))
            elif (self.color == 'white') and (self.color != piece.color):
                if ((piece.position[1] == self.position[1] - 1) and (
                        piece.position[0] == self.position[0] - 1 or piece.position[0] == self.position[0] + 1)):
                    moveList.append((pieceX, pieceY))

        return moveList
