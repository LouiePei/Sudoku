#finds next empty square (row, col)
def find_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:  #found empty
                return row, col

    #no empty spaces left
    return None, None

#determines whether a guess is valid
def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    col_vals = [puzzle[i][col] for i in range(9)]

    if guess in col_vals or guess in row_vals:  #check row and col
        return False        

    #make square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    #check square
    for row in range(row_start, row_start+3):
        for col in range(col_start, col_start+3):
            if puzzle[row][col] == guess:
                return False
    
    #number not in row, col, square
    return True

#solves sudoku given as a list with -1 representing empty space
def solve_sudoku(puzzle):
    row, col = find_empty(puzzle)

    
    if row is None:     #puzzle solved
        return puzzle
    
    #try value
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return puzzle

        puzzle[row][col] = -1 #reset guess
    
    return False    #sudoku is unsolvable