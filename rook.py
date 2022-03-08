import gamePiece


class rook(gamePiece.gamePiece):
    def __init__(self, color, position, width, height):
        if color == 'white':
            image = "1x/wrook.png"
        else:
            image = "1x/brook.png"
        super().__init__(color, position, image, width, height)

    def getMoves(self, friend, enemy):
        cordList = [[], []]
        enemy_stops = []
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
            cordList.sort()
            for i in range(len(friend)):
                if friend[i].position in cordList[0]:
                    cordList[0].remove(friend[i].position)
                    if friend[i].position != self.position:
                        limiter = True
            # for l in range(len(enemy)):
            #     if enemy[l].position in cordList[0]:
            #         limit = 8 - enemy[l].position[0]
            #         for i in range(limit):
            #             enemy_stops.append(cordList[0][i])
        print('row stops:', enemy_stops)
        #for i in range(len(enemy_stops))

        enemy_stops = []
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
            for i in range(len(friend)):
                if friend[i].position in cordList[1]:
                    cordList[1].remove(friend[i].position)
                    if friend[i].position != self.position:
                        limiter = True
            # for l in range(len(enemy)):
            #     if enemy[l].position in cordList[1]:
            #         limit = 8 - enemy[l].position[1]
            #         for i in range(limit):
            #             enemy_stops.append(cordList[1][i])

        print('Col stops: ', enemy_stops)
        return cordList
