from turtle import position
import pieces.gamePiece

class knight(pieces.gamePiece.gamePiece):
    def __init__(self, color, position, visible):
        if(color == 'white'):
            self.image = "pieces/images/wknight.png"
        elif (color == 'black'):
            self.image = "pieces/images/bknight.png"
        self.moves = 0
        super().__init__(self.image, color, position, visible, self.moves)
        
    def getMoves(self, all_pieces):
        # Get all possiable moves for piece
        moveList = []
        for y in range(8):
                for x in range(8):
                    move = (x,y)
                    if (move == (self.position[0] + 2, self.position[1] + 1)):
                        moveList.append((x,y))
                    elif (move == (self.position[0] - 2, self.position[1] + 1)):
                        moveList.append((x,y))
                    elif (move == (self.position[0] + 2, self.position[1] - 1)):
                        moveList.append((x,y))
                    elif (move == (self.position[0] - 2, self.position[1] - 1)):
                        moveList.append((x,y))
                    elif (move == (self.position[0] + 1, self.position[1] + 2)):
                        moveList.append((x,y))
                    elif (move == (self.position[0] - 1, self.position[1] + 2)):
                        moveList.append((x,y))
                    elif (move == (self.position[0] + 1, self.position[1] - 2)):
                        moveList.append((x,y))
                    elif (move == (self.position[0] - 1, self.position[1] - 2)):
                        moveList.append((x,y))
                    
        # Remove piece position from list
        if (self.position in moveList):
            moveList.remove(self.position)
    
        # remove other pieces position from list
        for piece in all_pieces:
            if(piece.visible == False):
                continue
            
            elif((piece.position in moveList) and (piece.color == self.color)):
                moveList.remove(piece.position)

        return moveList
    
    def setPosition(self, selectedPos):
        self.position = selectedPos
        self.moves += 1
        return(self.position)
    
    def setVisible(self, visible):
        self.visible = visible
        return(self.visible)