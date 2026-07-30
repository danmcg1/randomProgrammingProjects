
# Create a sudoku solver
# Initially just work on the code to check for the correct values
 # Next work on giving it a file/photo of a sudoku puzzle and having it generate the data from it

import numpy as np
import tabulate as tb

# -------------------- Easy puzzle ----------------------------
# sudokuTable = np.array([
#     [9,0,0,5,0,8,0,0,7],
#     [0,8,0,3,0,2,9,0,5],
#     [0,5,4,0,0,0,0,8,0],
#     [0,7,0,6,8,0,0,3,2],
#     [1,0,0,0,0,4,0,0,8],
#     [5,0,0,2,1,9,0,6,0],
#     [0,0,0,9,0,6,0,0,1],
#     [7,2,6,0,0,1,0,4,0],
#     [0,0,1,4,7,0,0,5,6],
# ])

# -------------------- Medium puzzle ----------------------------
# sudokuTable = np.array([
#     [2,0,3,4,0,0,0,0,5],
#     [8,0,9,1,6,0,7,0,4],
#     [0,0,6,0,3,0,0,1,9],
#     [7,0,2,0,0,3,0,6,0],
#     [0,0,8,2,5,0,0,0,0],
#     [0,0,1,6,0,7,0,0,2],
#     [0,0,7,0,0,5,9,2,6],
#     [9,3,0,7,2,0,0,0,0],
#     [6,0,0,0,9,0,4,7,0],
# ])

# -------------------- Hard puzzle ----------------------------
# sudokuTable = np.array([
#     [1,0,0,0,3,4,0,0,8],
#     [0,7,0,6,8,0,0,3,0],
#     [0,0,8,2,1,0,7,0,4],
#     [0,5,4,0,9,0,6,8,0],
#     [9,1,0,5,0,8,0,2,0],
#     [0,8,0,3,0,0,0,0,5],
#     [3,0,5,9,0,6,8,7,1],
#     [0,0,6,0,0,0,0,4,0],
#     [0,0,1,0,7,0,2,0,0],
# ])

# -------------------- Expert puzzle ----------------------------
# sudokuTable = np.array([
#     [1,5,0,0,8,2,0,0,0],
#     [3,0,0,0,7,0,0,1,0],
#     [0,0,0,0,0,0,7,5,3],
#     [0,0,0,5,2,7,6,0,9],
#     [0,0,0,0,0,0,5,0,0],
#     [0,4,0,0,6,3,8,0,7],
#     [4,0,0,0,0,8,0,0,0],
#     [7,0,3,0,4,0,1,0,0],
#     [0,0,8,6,0,0,3,0,0],
# ])

# -------------------- Master puzzle ----------------------------
# sudokuTable = np.array([
#     [0,7,0,0,4,5,2,9,0],
#     [0,4,3,7,2,0,5,0,0],
#     [6,0,0,0,9,0,7,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,5,0,0,0,0,0,4],
#     [2,3,0,0,7,9,8,0,0],
#     [7,0,0,0,0,0,0,0,0],
#     [0,1,9,0,8,0,0,0,0],
#     [0,8,0,2,0,4,0,1,0],
# ])

# -------------------- Extreme puzzle ----------------------------
sudokuTable = np.array([
    [0,5,0,0,0,0,0,0,0],
    [4,6,9,0,0,0,0,0,5],
    [0,0,0,0,0,9,3,0,0],
    [0,0,0,5,0,7,2,0,0],
    [1,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,0,0,1,0],
    [6,0,0,0,0,0,0,0,7],
    [7,0,4,2,0,0,1,0,0],
    [8,0,0,6,0,0,0,4,2],
])

table = sudokuTable

def findEmptyCells(table) -> list:
    emptyValues = []
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row, col] == 0:
                emptyValues.append((row,col))
    return(emptyValues)

def getCurrentZone(table, row, col) -> list:
    zoneRowStart = (row // 3) * 3 
    zoneColumnStart = (col // 3) * 3 
    currentZone = table[zoneRowStart : zoneRowStart + 3, zoneColumnStart : zoneColumnStart + 3]
    return(currentZone)


def isValueValidAtLocation(table, row, col, value) -> bool:
    fullRow = table[row]
    fullCol = table[:,col]
    fullZone = getCurrentZone(table,row,col).flatten()
    if value in fullRow or value in fullCol or value in fullZone:
        return(False)
    else:
        return(True)


def checkSimpleExclusiveEntries(table) -> list:
    for row, col in findEmptyCells(table):
        valid_options = []
        for num in range(1, len(table)+1):
            if isValueValidAtLocation(table,row,col,num) == True:
                valid_options.append(num)
        if len(valid_options) == 1:
            table[row,col] = valid_options[0]
    return(table)


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

def checkHiddenSinglesInZones(table) -> list:
    for zone_row in range(0, len(table), 3):
        for zone_col in range(0,len(table), 3):

            for num in range(1, len(table)+1):
                possible_cells = []
                # Scan ALL 9 cells in this 3x3 zone
                for r in range(zone_row, zone_row + 3):
                    for c in range(zone_col, zone_col + 3):
                        if table[r, c] == 0 and isValueValidAtLocation(table,r,c,num):
                            possible_cells.append((r,c))
                # After checking the full zone, evaluate the total matches
                if len(possible_cells) == 1:
                    target_r, target_c = possible_cells[0]
                    table[target_r, target_c] = num
    return(table)

def attemptSolve(table) -> bool:
    while 0 in table:
            empty_before = np.count_nonzero(table == 0)
            checkSimpleExclusiveEntries(table)
            checkHiddenSinglesInRows(table)
            checkHiddenSinglesInCols(table)
            checkHiddenSinglesInZones(table)
            empty_after = np.count_nonzero(table == 0)
            
            if empty_after == empty_before:
                return(False)
    return(True)


def recursiveSolve(table) -> list:
    empty_cells = findEmptyCells(table)

    # BASE CASE: If no empty cells remain puzzle is complete
    if not empty_cells:
        return True
        
    row, col = empty_cells[0]  # Focus only on the first empty cell
    
    for num in range(1, len(table) + 1):
        if isValueValidAtLocation(table, row, col, num):
            table[row, col] = num  # Step 1: Write down candidate number
            
            # Step 2: Pass the candidate n umber to the next "Worker"
            if recursiveSolve(table) == True:
                return True  # Correct. Pass 'True' up the chain.
                
            # Step 3: Backtrack. If the worker returned False, erase and try next num
            table[row, col] = 0
            
    # If we tried 1 through 9 and none worked, return False to the previous worker
    return False


                          
def main():
    attemptSolve(table)
    if 0 in table:
            print("\nSolution reached via purely logical processes")
            print(tb.tabulate(table, tablefmt="grid"))
            print("\nLogical solver stuck — finishing with recursive backtracking...\n")
            recursiveSolve(table)
            
    print(tb.tabulate(table, tablefmt="grid"))


if __name__ == '__main__':
    main()