
# Create a sudoku solver
# Initially just work on the code to check for the correct values
 # Next work on giving it a file/photo of a sudoku puzzle and having it generate the data from it

import numpy as np
import tabulate as tb

class additionCell:
    def __init__(self, total, cell1, cell2):
        self.total = total
        self.cell1 = cell1
        self.cell2 = cell2


# -------------------- Waffle puzzle ----------------------------
numberWafflePuzzle = np.array([
    [0,0,4,0,1,0,0],
    [0,3,0,7,0,8,0],
    [7,0,3,2,6,0,5],
    [0,11,0,8,0,5,0],
    [2,0,1,7,3,0,4],
    [0,12,0,10,0,8,0],
    [0,0,7,0,2,0,0],
])

rel = {
    "u": (-1,0),
    "d": (1,0),
    "l": (0,-1),
    "r": (0,1)
}

numberWafflePuzzle = np.array([
    [0,0,4,0,1,0,0],
    [0,additionCell(3, rel["u"], rel["l"]),0,additionCell(7, rel["u"], rel["l"]),0,additionCell(8, rel["u"], rel["r"]),0],
    [7,0,3,2,6,0,5],
    [0,additionCell(11, rel["l"], rel["d"]),0,additionCell(8, rel["l"], rel["u"]),0,additionCell(5, rel["u"], rel["l"]),0],
    [2,0,1,7,3,0,4],
    [0,additionCell(12, rel["d"], rel["l"]),0,additionCell(10, rel["d"], rel["l"]),0,additionCell(8, rel["d"], rel["r"]),0],
    [0,0,7,0,2,0,0],
])




table = numberWafflePuzzle.copy()

def findEmptyCells(table) -> list:
    emptyValues = []
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row] [col] == 0:
                emptyValues.append((row,col))
    return(emptyValues)


def isValueValidAtLocation(table, row, col, value) -> bool:
    fullRow = table[row]
    fullCol = [table[r][col] for r in range(len(table))]
    return value not in fullRow and value not in fullCol


def checkSimpleExclusiveEntries(table) -> list:
    for row, col in findEmptyCells(table):
        valid_options = []
        for num in range(1, len(table)+1):
            if isValueValidAtLocation(table,row,col,num) == True:
                valid_options.append(num)
        if len(valid_options) == 1:
            table[row,col] = valid_options[0]
    return(table)         

def checkAddition(table, sum, coord1, coord2) -> bool:
    if table(coord1) + table(coord2) == sum:
        return True
    else:
        return False
    


def checkHiddenSinglesInRows(table) -> list:
    for row in range(len(table)):
        for num in range(1, len(table) + 1):
            possible_cols = []
            for col in range(len(table)):
                 if table[row, col] == 0 and isValueValidAtLocation(table, row, col, num) == 1:
                    possible_cols.append(col)
            if len(possible_cols) == 1:
                table[row,possible_cols[0]] = num
    return(table)

def checkHiddenSinglesInCols(table) -> list:
    for col in range(len(table)):
        for num in range(1, len(table) + 1):
            possible_rows = []
            for row in range(len(table)):
                if table[row, col] == 0 and isValueValidAtLocation(table, row, col, num) == 1:
                    possible_rows.append(row)
            if len(possible_rows) == 1:
                table[possible_rows[0],col] = num
    return(table)


def attemptSolve(table) -> bool:
    while 0 in table:
            empty_before = np.count_nonzero(table == 0)
            checkSimpleExclusiveEntries(table)
            # checkHiddenSinglesInRows(table)
            # checkHiddenSinglesInCols(table)
            empty_after = np.count_nonzero(table == 0)
            
            if empty_after == empty_before:
                return(False)
    return(True)


def recursiveSolve(table) -> bool:
    empty_cells = findEmptyCells(table)

    # BASE CASE: If no empty cells remain, the puzzle is complete
    if not empty_cells:
        return True
        
    row, col = empty_cells[0]  # Focus on the first empty cell
    
    for num in range(1, len(table) + 1):
        if isValueValidAtLocation(table, row, col, num):
            table[row][col] = num  # Step 1: Place candidate number
            
            # Step 2: Recurse to solve the rest of the board
            if recursiveSolve(table):
                return True  # Solution found!
                
            # Step 3: Backtrack (reset cell using list indexing)
            table[row][col] = 0
            
    # Tried 1 through 9 and none worked -> trigger backtrack in caller
    return False


                          
def main():

    print(tb.tabulate(table, tablefmt="grid"))
    print("\n")

    for i in range(5):
        attemptSolve(table)

    print(tb.tabulate(table, tablefmt="grid"))
    
    # if any(0 in row for row in table):
    #     print("\nLogical solver stuck — finishing with recursive backtracking...\n")
    #     recursiveSolve(table)
    # else:
    #     print("\nSolution reached via purely logical processes!")
            
    # print(tb.tabulate(table, tablefmt="grid"))

if __name__ == "__main__":
    main()