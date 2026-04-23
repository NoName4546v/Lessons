board = ["5","3",".",".","7",".",".",".","."
        ,"6",".",".","1","9","5",".",".","."
        ,".","9","8",".",".",".",".","6","."
        ,"8",".",".",".","6",".",".",".","3"
        ,"4",".",".","8",".","3",".",".","1"
        ,"7",".",".",".","2",".",".",".","6"
        ,".","6",".",".",".",".","2","8","."
        ,".",".",".","4","1","9",".",".","5"
        ,".",".",".",".","8",".",".","7","9"]

horizontal = []
vertical = []
cube = []

while True:
    for i in board:
        #Горизонталь
        if board.index(i) < 9:
            for a in range(0, 8):
                if a != ".":
                    horizontal.append(a)
        elif board.index(i) < 18 and board.index(i)> 8:
            for a in range(8, 17):
                if a != ".":
                    horizontal.append(a)
        elif board.index(i) < 27 and board.index(i)> 17:
            for a in range(17, 26):
                if a != ".":
                    horizontal.append(a)
        elif board.index(i) < 36 and board.index(i)> 26:
            for a in range(26, 35):
                if a != ".":
                    horizontal.append(a)
        elif board.index(i) < 45 and board.index(i)> 35:
            for a in range(35, 44):
                if a != ".":
                    horizontal.append(a)
        elif board.index(i) < 54 and board.index(i)> 44:
            for a in range(44, 53):
                if a != ".":
                    horizontal.append(a)
        elif board.index(i) < 54 and board.index(i)> 53:
            for a in range(53, 62):
                if a != ".":
                    horizontal.append(a)
        elif board.index(i) < 54 and board.index(i)> 62:
            for a in range(62, 71):
                if a != ".":
                    horizontal.append(a)
        elif board.index(i) < 54 and board.index(i)> 71:
            for a in range(71, 80):
                if a != ".":
                    horizontal.append(a)

        #Вертикаль