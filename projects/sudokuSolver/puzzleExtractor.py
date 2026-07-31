import cv2 as cv2 
import easyocr as eocr

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


def getMainContour(image_thresh) -> list:
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
    main_contour = cv2.drawContours(img_copy, [puzzle_contour], -1, (0, 255, 0), 5)




    print(len(contours))
    cv2.drawContours(main_contour, contours, -1, (0, 255, 0), 20)

    cv2.imshow("All Contours", main_contour)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image_data = imageImport()
    image_thresholded = thresholdImage(image_data)
    getMainContour(image_thresholded)

if __name__ == '__main__':
    main()