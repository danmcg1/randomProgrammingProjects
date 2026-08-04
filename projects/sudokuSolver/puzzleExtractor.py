import cv2 as cv2 
import easyocr
import numpy as np

def imageImport():
    image_file = 'sudoku-clean.png'
    image_data = cv2.imread(image_file,0)
    if image_data is None:
        print('No valid image file located')
    else:
        print('Image loaded successfully\n')
    return(image_data)


def thresholdImage(image: list):
    image_thresholded = cv2.adaptiveThreshold(
        image,
        255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 
        11, 
        2
    )
    return(image_thresholded)


def getMainContour(image_thresh) -> list:
    contours, hierarchy = cv2.findContours(
    image_thresh, 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE
    )

    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

    

    for c in sorted_contours:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
        if len(approx) == 4:
            puzzle_contour = approx
            break
    
    return(puzzle_contour)

    # main_contour = cv2.drawContours(img_copy, [puzzle_contour], -1, (0, 255, 0), 5)
    # print(len(contours))
    # cv2.drawContours(main_contour, contours, -1, (0, 255, 0), 20)

def flattenImage(source_img, main_contour, output_size=450) -> list:
    pts = main_contour.reshape(4,2)
    coordinates = np.zeros((4,2), dtype="float32")

    s = pts.sum(axis=1)
    coordinates[0] = pts[np.argmin(s)]  # Top-Left has smallest sum
    coordinates[2] = pts[np.argmax(s)]  # Bottom-Right has largest sum

    diff = np.diff(pts, axis=1)
    coordinates[1] = pts[np.argmin(diff)]  # Top-Right has smallest difference
    coordinates[3] = pts[np.argmax(diff)]  # Bottom-Left has largest difference

    dst = np.array([
        [0, 0],
        [output_size - 1, 0],
        [output_size - 1, output_size - 1],
        [0, output_size - 1]
    ], dtype="float32")

    matrix = cv2.getPerspectiveTransform(coordinates, dst)
    flattened_img = cv2.warpPerspective(source_img, matrix, (output_size, output_size))
    return(flattened_img)
    # cv2.imshow("Fixed perspective image", flattened_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def getCellContents(flattened_img, grid_size = 9, margin=3) -> list:
    
    img_h, img_w = flattened_img.shape[:2]
    cell_height = img_h // grid_size
    cell_width = img_w // grid_size
    

    cells = []
    for row in range(9):
        row_cells = []
        for col in range(9):
            y1 = row * cell_height
            y2 = (row +1) * cell_height
            x1 = col * cell_width
            x2 = (col + 1) * cell_width

            
            cell = flattened_img[y1:y2, x1:x2]
            clean_cell = cell[margin:-margin, margin:-margin]

            row_cells.append(clean_cell)
        cells.append(row_cells)

    return(cells)

    # cv2.imshow("Cell 0,3", cells[0][3])
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def build_sudoku_board(cell_array) -> list:
    reader = easyocr.Reader(['en'], gpu=False)
    board = []
    for r in range(9):
        row_values = []
        for c in range(9):
            cell = cell_array[r][c]
            
            # 1. Check if the cell is blank
            # (Adjust the 40 pixel threshold up/down depending on your image resolution)
            if np.count_nonzero(cell > 100) < 40:
                row_values.append(0)
                continue
            
            # 2. Run EasyOCR on non-blank cells
            results = reader.readtext(cell, allowlist='123456789', detail=0)
            
            if results:
                # Store the first recognized digit
                row_values.append(int(results[0]))
            else:
                # Fallback if OCR failed to find a clean digit
                row_values.append(0)
                
        board.append(row_values)
        
    return board
        


def main():
    img_data = imageImport()
    img_copy = img_data.copy()
    image_thresholded = thresholdImage(img_data)
    main_contour = getMainContour(image_thresholded)
    flattened_img = flattenImage(img_copy, main_contour)
    cell_array = getCellContents(flattened_img)
    sudoku_board = build_sudoku_board(cell_array)

    return sudoku_board



if __name__ == '__main__':
    # Running directly will extract and print the board to terminal
    board = main()
    for row in board:
        print(row)