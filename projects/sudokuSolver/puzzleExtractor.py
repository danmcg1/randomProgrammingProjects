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

def preprocess_cell(cell_img):
    """
    Cleans, threshold, pads, and resizes a single cell image for OCR.
    Returns (processed_image, digit_pixel_count)
    """
    # 1. Convert to grayscale if BGR
    if len(cell_img.shape) == 3:
        gray = cv2.cvtColor(cell_img, cv2.COLOR_BGR2GRAY)
    else:
        gray = cell_img.copy()

    # 2. Otsu thresholding: text becomes white (255), background black (0)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 3. Count white (digit) pixels
    digit_pixel_count = cv2.countNonZero(thresh)

    # 4. Invert back to black text on white background for EasyOCR
    inverted = cv2.bitwise_not(thresh)

    # 5. Add a 15px white border padding so EasyOCR sees a isolated character
    padded = cv2.copyMakeBorder(
        inverted, 15, 15, 15, 15, 
        borderType=cv2.BORDER_CONSTANT, 
        value=[255, 255, 255]
    )

    # 6. Resize up to 100x100 pixels for better OCR feature extraction
    resized = cv2.resize(padded, (100, 100), interpolation=cv2.INTER_CUBIC)

    return resized, digit_pixel_count

def build_sudoku_board(cells, min_pixel_threshold=20):
    board = []

    for r in range(9):
        row_values = []
        for c in range(9):
            raw_cell = cells[r][c]

            # Preprocess the cell image
            processed_cell, digit_pixels = preprocess_cell(raw_cell)

            # Check if the cell is blank (thin font digits typically have 30-150 pixels)
            if digit_pixels < min_pixel_threshold:
                row_values.append(0)
                continue

            # Run EasyOCR with character allowlist
            results = reader.readtext(
                processed_cell, 
                allowlist='123456789', 
                detail=0, 
                psm=10
            )

            if results:
                row_values.append(int(results[0]))
            else:
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