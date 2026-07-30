
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
sudokuTable = np.array([
    [1,5,0,0,8,2,0,0,0],
    [3,0,0,0,7,0,0,1,0],
    [0,0,0,0,0,0,7,5,3],
    [0,0,0,5,2,7,6,0,9],
    [0,0,0,0,0,0,5,0,0],
    [0,4,0,0,6,3,8,0,7],
    [4,0,0,0,0,8,0,0,0],
    [7,0,3,0,4,0,1,0,0],
    [0,0,8,6,0,0,3,0,0],
])

table = sudokuTable

def findEmptyCells(table) -> list:
    emptyValues = []
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row, col] == 0:
                emptyValues.append((row,col))
    return(emptyValues)

def getCurrentRowGroup (table, row) -> list:
    rowStart = (row // 3) * 3
    currentRowGroup = table[rowStart : rowStart + 3]
    return(currentRowGroup)

def getCurrentColGroup (table, col) -> list:
    colStart = (col // 3) * 3
    currentColGroup = table[:,colStart : colStart + 3]
    return(currentColGroup)

def getCurrentZone(table, row, col):
    zoneRowStart = (row // 3) * 3 
    zoneColumnStart = (col // 3) * 3 
    currentZone = table[zoneRowStart : zoneRowStart + 3, zoneColumnStart : zoneColumnStart + 3]
    return(currentZone)


def isValueValidAtLocation(table, row, col, value):
    fullRow = table[row]
    fullCol = table[:,col]
    fullZone = getCurrentZone(table,row,col).flatten()
    if value in fullRow or value in fullCol or value in fullZone:
        return(False)
    else:
        return(True)


def checkSimpleExclusiveEntries(table):
    for row, col in findEmptyCells(table):
        valid_options = []
        for num in range(1, len(table)+1):
            if isValueValidAtLocation(table,row,col,num) == True:
                valid_options.append(num)
        if len(valid_options) == 1:
            table[row,col] = valid_options[0]
    return(table)

# def checkRowGroups(table):
#     for row, col in findEmptyCells(table):
#         for num in range(1, len(table)+1):


def main():
    for i in range(len(table)):
        checkSimpleExclusiveEntries(table)
        if 0 not in table:
            break

    print(tb.tabulate(table,tablefmt="grid"))



if __name__ == '__main__':
    main()