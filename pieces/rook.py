import pieces.gamePiece

class rook(pieces.gamePiece.gamePiece):
    def __init__(self, color, position, screenSize, visible):
        if(color == 'white'):
            self.image = "pieces/images/wrook.png"
        elif (color == 'black'):
            self.image = "pieces/images/brook.png"
        super().__init__(self.image, color, position, screenSize, visible)
        
    def getMoves(self):
        
        cordList = []
        for y in range(8):
                for x in range(8):
                    
                    if (x == self.position[0]):
                        cordList.append((x,y))
                    elif (y == self.position[1]):
                        cordList.append((x,y))
                    
        if (self.position in cordList):
            cordList.remove(self.position)
        return cordList
    
    def setPosition(self, selectedPos):
        self.position = selectedPos
        return(self.position)
    