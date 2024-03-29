import sys
import pieces.GamePiece


class King(pieces.GamePiece.GamePiece):
    def __init__(self, color, position, visible):
        if (color == 'white'):
            self.imageFile = "pieces/images/wking.png"
        elif (color == 'black'):
            self.imageFile = "pieces/images/bking.png"
        self.moves = 0
        self.name = type(self).__name__
        self.id = type(self).__name__ + str(position[0]) + str(position[1])
        super().__init__(self.imageFile, color, position, visible, self.moves)

    def getMoves(self):
        # Get all possible moves for piece
        moveList = []
        for y in range(8):
            for x in range(8):
                move = (x, y)

                if (move == (self.position[0] + 1, self.position[1] + 1)):
                    moveList.append(move)
                elif (move == (self.position[0] - 1, self.position[1] + 1)):
                    moveList.append(move)
                elif (move == (self.position[0] + 1, self.position[1] - 1)):
                    moveList.append(move)
                elif (move == (self.position[0] - 1, self.position[1] - 1)):
                    moveList.append(move)
                elif (move == (self.position[0] + 1, self.position[1])):
                    moveList.append(move)
                elif (move == (self.position[0] - 1, self.position[1])):
                    moveList.append(move)
                elif (move == (self.position[0], self.position[1] + 1)):
                    moveList.append(move)
                elif (move == (self.position[0], self.position[1] - 1)):
                    moveList.append(move)

        # Remove piece position from list
        if (self.position in moveList):
            moveList.remove(self.position)

        # moves based on other pieces
        for piece in self.all_pieces:

            # Castling
            if (type(piece).__name__ == "Rook" and piece.getColor() == self.color):
                if ((self.moves == 0) and (piece.moves == 0)):
                    pieceX, pieceY = piece.getPosition()
                    x, y = self.position
                    if (pieceX > x):
                        moveList.append((pieceX - 1, y))
                    elif (pieceX < x):
                        moveList.append((pieceX + 1, y))

        for piece in self.all_pieces:
            # remove other friendly pieces position from list
            if ((piece.getPosition() in moveList) and (piece.getColor() == self.color)):
                moveList.remove(piece.getPosition())

            # Remove self-checking moves
            if ((piece.getColor() != self.color) and (sys._getframe(1).f_code.co_name != "getMoves")):
                pieceMoves = piece.getMoves()
                for move in pieceMoves:
                    if move in moveList:
                        moveList.remove(move)

        return moveList
