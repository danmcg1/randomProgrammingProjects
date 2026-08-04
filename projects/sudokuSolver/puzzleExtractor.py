import cv2 as cv2 
import easyocr as eocr
import numpy as np

def imageImport():
    image_file = 'sudoku.png'
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


def getMainContour(img_copy, image_thresh) -> list:
    img_copy = imageImport().copy()
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
    fixed_perspective_img = cv2.warpPerspective(source_img, matrix, (output_size, output_size))
    cv2.imshow("Fixed perspective image", fixed_perspective_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    img_data = imageImport()
    img_copy = imageImport()
    image_thresholded = thresholdImage(img_data)
    main_contour = getMainContour(img_copy, image_thresholded)
    flattenImage(img_copy, main_contour)

if __name__ == '__main__':
    main()