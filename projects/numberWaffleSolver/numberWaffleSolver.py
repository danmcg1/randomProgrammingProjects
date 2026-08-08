
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

    def __repr__(self):
            # Returns a placeholder string when printed
            return " . "  # or "   " for a blank space


# -------------------- Waffle puzzle ----------------------------
# numberWafflePuzzle = np.array([
#     [0,0,4,0,1,0,0],
#     [0,3,0,7,0,8,0],
#     [7,0,3,2,6,0,5],
#     [0,11,0,8,0,5,0],
#     [2,0,1,7,3,0,4],
#     [0,12,0,10,0,8,0],
#     [0,0,7,0,2,0,0],
# ])

rel = {
    "u": (-1,0),
    "d": (1,0),
    "l": (0,-1),
    "r": (0,1)
}

numberWafflePuzzle = np.array([
    [4,0,3,0,7,0,0],
    [0,additionCell(7, rel["d"], rel["l"]),0,additionCell(9, rel["u"], rel["l"]),0,additionCell(7, rel["u"], rel["l"]),0],
    [1,0,6,0,3,0,7],
    [0,additionCell(7, rel["r"], rel["d"]),0,additionCell(6, rel["u"], rel["r"]),0,additionCell(8, rel["r"], rel["d"]),0],
    [7,0,1,0,5,0,3],
    [0,additionCell(5, rel["l"], rel["d"]),0,additionCell(8, rel["u"], rel["l"]),0,additionCell(7, rel["d"], rel["l"]),0],
    [0,0,2,0,4,0,0],
])

table = numberWafflePuzzle.copy()

def extractAdditionCells(table) -> list:
    constraintCells = []
    
    for row in range(1, len(table), 2):
        for col in range(1, len(table), 2):
            cell = table[row, col]
            
            coord1 = (row + cell.cell1[0], col + cell.cell1[1])
            coord2 = (row + cell.cell2[0], col + cell.cell2[1])
            
            constraintCells.append((cell.total, coord1, coord2))
            
    return constraintCells


def findEmptyCells(table) -> list:
    emptyValues = []
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row] [col] == 0:
                emptyValues.append((row,col))
    return(emptyValues)


def isValueValidAtLocation(table, row, col, value) -> bool:
    if row % 2 == 0:
        if value in table[row]:
            return False

    if col % 2 == 0:
        column_vals = [table[r][col] for r in range(len(table))]
        if value in column_vals:
            return False

    return True


def checkSimpleExclusiveEntries(table) -> list:
    for row, col in findEmptyCells(table):
        valid_options = []
        for num in range(1, len(table)+1):
            if isValueValidAtLocation(table,row,col,num) == True:
                valid_options.append(num)
        if len(valid_options) == 1:
            table[row,col] = valid_options[0]
    return(table)         


def check_addition_constraint(table, constraint) -> bool:
    sum, coord1, coord2 = constraint
    val1 = table[coord1]
    val2 = table[coord2]
    
    if val1 != 0 and val2 != 0:
        return (val1 + val2) == sum
        
    return True  

def are_all_additions_valid(table, constraints) -> bool:
    for constraint in constraints:
        if not check_addition_constraint(table, constraint):
            return False
    return True



def recursiveSolve(table, constraints) -> bool:
    empty_cells = findEmptyCells(table)

    if not empty_cells:
        return True
        
    row, col = empty_cells[0] 
    
    for num in range(1, len(table) + 1):
        if isValueValidAtLocation(table, row, col, num):
            table[row, col] = num
            if not are_all_additions_valid(table, constraints):
                pass
            
            if are_all_additions_valid(table, constraints):
                if recursiveSolve(table, constraints):
                    return True  
                    
            table[row, col] = 0
            
    return False  


                          
def main():
    constraintCells = extractAdditionCells(table)

    print("--- Starting Board ---")
    print(tb.tabulate(table, tablefmt="grid"))
    print("\n")
   
    recursiveSolve(table, constraintCells)
            
    print("--- Ending Board ---")
    print(tb.tabulate(table, tablefmt="grid"))

if __name__ == "__main__":
    main()