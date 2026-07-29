
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


def checkIfValueInZone(grid, row, col):

    # Given any cell at row 4, col 7:
    #row, col = 8, 2

    # Calculate the top-left corner of its 3x3 box
    box_row_start = (row // 3) * 3  # (4 // 3) * 3 = 3
    box_col_start = (col // 3) * 3  # (7 // 3) * 3 = 6

    # Slice the 3x3 box dynamically
    current_box = grid[box_row_start : box_row_start + 3, box_col_start : box_col_start + 3]

    # Check if a candidate number is already in that box
    print(current_box)


def findEmptyCells(grid):
    for row in range(9):
        for col in range(9):
            if grid[row, col] == 0:
                # Found an empty cell to solve!
                pass

def main():
    checkIfValueInZone(sudokuTable, 8,2)

if __name__ == '__main__':
    main()