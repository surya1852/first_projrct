# DEVELOPMENT OF MACHINE LEARNING MODEL FOR VEHICLE NUMBER PLATE RECOGNITION IN HAZY ENVIRONMENT.
## Introduction
This project develops a machine learning model for Vehicle Number Plate Recognition (VNPR) in hazy environments using YOLOv8. The model is designed to detect and recognize vehicle number plates even when the images are affected by haze. The project includes four primary Python scripts for dehazing, detecting the number plate, and extracting the characters from the plate.

## Installation instructions
Python IDLE
OCR
yoloV8

## Project Structure
1. __init__.py: The main object for dehazing images.
2. 1run.py: Detects and processes grey-scaled and haze-corrected images using the dehazing functionality from init.py.
3. 2run.py: Detects the vehicle number plate and extracts the number plate text (letters and digits).
4. extract.py: Displays the extracted vehicle number plate number and alphabets on the image, showing them only within the detected number plate area.

## Usage
1. Dehazing an image: To dehaze an image, you run __init__.py directly
   ### method1
   ```
     python _init_.py --input image_path --output dehazed_image_path
   ```
2. Detecting and processing the image: Use 1run.py for detecting vehicle number plates in grey-scaled and haze-corrected images:
   ### method2
   ```
     python 1run.py --input dehazed_image_path
   ```
3. Detecting and extracting the vehicle number plate: Use 2run.py to detect the number plate and extract the number:
   ### method3
   ```
   python 2run.py --input image_path
   ```
4. Displaying extracted number plate information: Use extract.py to display the detected numbers and alphabets in the number plate:
   ### method4
   ```
   python extract.py --input detected_image_path
   ```
## Results
   The results of the project are stored in specific folders for easy access:

   1. Dehazed Images:
     The dehazed versions of input images, processed by init.py, are saved in the outputimages folder.
   2. Number Plate Detection Outputs:
     The outputs of detecting vehicle number plates, processed by 2run.py, are stored in the runs folder.
     This folder contains subfolders with the detection results, including the bounding boxes around number plates and extracted text.
## Example ouput flow
  1. Input Image → Processed using init.py → Dehazed Image (stored in outputimages).
  2. Dehazed Image → Processed using 2run.py → Detected Number Plates (stored in runs).



   



