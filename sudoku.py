board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

def horizontal_find(str):
    horizontal = []
    for i in board[str]:
        if i != ".":
            horizontal.append(i)
    return horizontal

def vertical_find(board, a):
    vertical = []
    for i in range(0, 8):
        if board[i][a] != ".":
            vertical.append(board[i][a])
    return vertical

def cube_find(board, line, col):
    cube = []
    lines = board[3*line : 3*line+3]
    for i in lines:
        columns = i[3*col : 3*col+3]
        while "." in columns:
            columns.remove(".")
        cube.extend(columns)
    return cube

def invert_list(list):
    list_2 = []
    for i in range(1, 10):
        if str(i) not in list:
            list_2.append(i)
    return list_2

def find_num(vert, horiz, cube):
    res = []
    tmp_list = min(vert, horiz, cube,key=len)
    for i in tmp_list:
        if i in vert and i in horiz and i in cube:
            res.append(i)
    return res

for i in board:
    for a in i:
        if a == ".":
            print(i.index(a), board.index(i),vertical_find(board, i.index(a)), horizontal_find(board.index(i)), cube_find(board, board.index(i)//3, i.index(a)//3))