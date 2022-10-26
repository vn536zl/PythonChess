import pieces.gamePiece

class bishop(pieces.gamePiece.gamePiece):
    def __init__(self, color, position, visible):
        if(color == 'white'):
            self.image = "pieces/images/wbishop.png"
        elif (color == 'black'):
            self.image = "pieces/images/bbishop.png"
        self.moves = 0
        super().__init__(self.image, color, position, visible, self.moves)
        
    def getMoves(self, all_pieces):
        # Get all possiable moves for piece
        moveList = []
        for y in range(8):
                for x in range(8):
                    move = (x,y)
                    i = 1
                    while(i < 8):
                        if(move == (self.position[0] + i, self.position[1] + i)):
                            moveList.append(move)
                        elif(move == (self.position[0] - i, self.position[1] + i)):
                            moveList.append(move)
                        elif(move == (self.position[0] + i, self.position[1] - i)):
                            moveList.append(move)
                        elif(move == (self.position[0] - i, self.position[1] - i)):
                            moveList.append(move)
                        i += 1
               
        # Remove piece position from list
        if (self.position in moveList):
            moveList.remove(self.position)
    
        # remove other pieces position from list
        for piece in all_pieces:
            if(piece.visible == False):
                continue
            
            if((piece.position in moveList) and (piece.color == self.color)):
                moveList.remove(piece.position)
            
            pieceX = piece.position[0]
            pieceY = piece.position[1]
            
            # Remove Top Right positions where another piece is in the way
            if((piece.position[0] > self.position[0]) and (piece.position[1] < self.position[1])):
                while((piece.position[0] <= pieceX <= 7) and (piece.position[1] >= pieceY >= 0)):
                    pieceX += 1
                    pieceY -= 1
                    if ((pieceX, pieceY) in moveList):
                        moveList.remove((pieceX, pieceY))
                        
            # Remove Top Left positions where another piece is in the way     
            if((piece.position[0] < self.position[0]) and (piece.position[1] < self.position[1])):
                while((piece.position[0] >= pieceX >= 0) and (piece.position[1] >= pieceY >= 0)):
                    pieceX -= 1
                    pieceY -= 1
                    if ((pieceX, pieceY) in moveList):
                        moveList.remove((pieceX, pieceY))
            
            # Remove Bottom Right positions where another piece is in the way
            if((piece.position[0] > self.position[0]) and (piece.position[1] > self.position[1])):
                while((piece.position[0] <= pieceX <= 7) and (piece.position[1] <= pieceY <= 7)):
                    pieceX += 1
                    pieceY += 1
                    if ((pieceX, pieceY) in moveList):
                        moveList.remove((pieceX, pieceY))
                        
            # Remove Bottom Left positions where another piece is in the way
            if((piece.position[0] < self.position[0]) and (piece.position[1] > self.position[1])):
                while((piece.position[0] >= pieceX >= 0) and (piece.position[1] <= pieceY <= 7)):
                    pieceX -= 1
                    pieceY += 1
                    if ((pieceX, pieceY) in moveList):
                        moveList.remove((pieceX, pieceY))

        return moveList
    
    def setPosition(self, selectedPos):
        self.position = selectedPos
        self.moves += 1
        return(self.position)
    
    def setVisible(self, visible):
        self.visible = visible
        return(self.visible)