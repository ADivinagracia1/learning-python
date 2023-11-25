def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    block = [[set() for _ in range(3)] for _ in range(3)]

    # print(rows)
    # print(cols)
    # print(block)

    for i in range(9): # row
        for j in range(9): # col
            cursor = board[i][j]
            if board[i][j] == '.':
                continue
            elif (cursor in rows[i]) or (cursor in cols[j]) or (cursor in block[i//3][j//3]):
                return False
            else:
                # Do something else
                # Check for validity here
                rows[i].add(cursor)
                cols[j].add(cursor)
                block[i//3][j//3].add(cursor)

    # print(rows)
    # print(cols)
    for block_i in block:
        print(block_i)


    return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6","8",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

va = isValidSudoku(board)
print(va)