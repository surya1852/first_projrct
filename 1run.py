import cv2
import image_dehazer

if __name__ == "__main__":

    HazeImg = cv2.imread('4.png')						# read input image -- (**must be a color image**)
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)		# Remove Haze

    						# display the original hazy image
    			# display the result
    cv2.imshow('grey scaled image', haze_map);						# display the original hazy image
    cv2.imshow('enhanced image', HazeCorrectedImg);			# display the result
    cv2.waitKey(0)
    cv2.imwrite("outputImages/result.jpg", HazeCorrectedImg)


