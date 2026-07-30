
# Create a sudoku solver
# Initially just work on the code to check for the correct values
 # Next work on giving it a file/photo of a sudoku puzzle and having it generate the data from it

import numpy as np

sudokuTable = np.array([
    [9,0,0,5,0,8,0,0,7],
    [0,8,0,3,0,2,9,0,5],
    [0,5,4,0,0,0,0,8,0],
    [0,7,0,6,8,0,0,3,2],
    [1,0,0,0,0,4,0,0,8],
    [5,0,0,2,1,9,0,6,0],
    [0,0,0,9,0,6,0,0,1],
    [7,2,6,0,0,1,0,4,0],
    [0,0,1,4,7,0,0,5,6],
])

rowGroup1 = sudokuTable[0:3]
rowGroup2 = sudokuTable[3:6]
rowGroup3 = sudokuTable[6:9]

columnGroup1 = sudokuTable[:,0:3]
columnGroup2 = sudokuTable[:,3:6]
columnGroup3 = sudokuTable[:,6:9]

zoneA1 = sudokuTable[0:3, 0:3]
zoneA2 = sudokuTable[0:3, 3:6]
zoneA3 = sudokuTable[0:3, 6:9]
zoneB1 = sudokuTable[3:6, 0:3]
zoneB2 = sudokuTable[3:6, 3:6]
zoneB3 = sudokuTable[3:6, 6:9]
zoneC1 = sudokuTable[6:9, 0:3]
zoneC2 = sudokuTable[6:9, 3:6]
zoneC3 = sudokuTable[6:9, 6:9]

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


def checkSimpleEntries(table):
    for row, col in findEmptyCells(table):
        valid_options = []
        for num in range(1, len(table)+1):
            if isValueValidAtLocation(table,row,col,num) == True:
                valid_options.append(num)
        if len(valid_options) == 1:
            table[row,col] = valid_options[0]
    return(table)




def main():
    while 0 in table:
        checkSimpleEntries(table)
    print(table)



if __name__ == '__main__':
    main()