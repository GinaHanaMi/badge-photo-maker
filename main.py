from PIL import Image
from rembg import remove
import os
import glob
import cv2
import numpy as np
import shutil
import os.path
import pathlib


#CREATES SOME VARIABLES FOR REFERENCE
work_dir = os.getcwd()
haarcascade = fr"{work_dir}\haarcascade\haarcascade_frontalface_default.xml"

#DEFINES THE SIZE OF IMAGE / PERSON FOR THE BADGE
new_id_size = (480, 640)

# DEFINE A LIST OF VALID IMAGE FILE EXTENSIONS
valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# SPECIFY THE FOLDER PATH WHERE YOU WANT TO SEARCH FOR IMAGE FILES TO PROCESS
input_img_path = fr'{work_dir}\inputImg'

# INITIALIZE AN EMPTY LIST TO STORE THE IMAGE FILE PATHS
image_files = []
image_file_names = []

# USE THE GLOB MODULE TO SEARCH FOR FILES IN THE SPECIFIED FOLDER
for extension in valid_extensions:
    image_files.extend(glob.glob(os.path.join(input_img_path, f'*{extension}')))
for file_path in image_files:
    image_file_names.append(os.path.basename(file_path))
    

# INITIALIZE THE FACE DETECTION MODEL
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
for i in range(len(image_files)):
    input_img = Image.open(image_files[i])
    # Remove background using rembg library
    input_img = remove(input_img)
    input_img = remove(input_img) #done two times for better result (much slower bcs of that)
    # Convert the image to grayscale
    bw_image = input_img.convert('L')
    no_bckg_img = remove(bw_image) #done once again - these parts can be changed for your needs
    # Load the grayscale image as a numpy array
    img_np = np.array(input_img)
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(img_np, scaleFactor=1.05, minNeighbors=10, minSize=(100, 100))
    # Check if any faces were detected
    if len(faces) > 0:
        # Process the first detected face (index 0)
        x, y, w, h = faces[0] # Get the first detected face
        #defines the offset of that detection
        x -= int(0.1 * w)
        y -= int(0.2 * h)
        w += int(0.3 * w)
        h += int(0.5 * h)
        x = max(0, x)
        y = max(0, y)
        cropped_face = img_np[y:y + h, x:x + w].copy() # Create a copy of the cropped face
        # Iterate through the copied cropped face and replace black pixels with white
        for x in range(cropped_face.shape[0]):
            for y in range(cropped_face.shape[1]):
                if (cropped_face[x, y] == 0).all():
                    cropped_face[x, y] = 255 # Replace black with white (255)
        cropped_face_pil = Image.fromarray(cropped_face)
        cropped_face_pil = cropped_face_pil.convert('L') #converts to black-white again
        cropped_face_pil = cropped_face_pil.resize(new_id_size)
        output_file_path = fr'{work_dir}\outputImg\{image_file_names[i]}{i}_face1.png'
        cropped_face_pil.save(output_file_path)
    else:
        # No faces detected, save the black and white image with background removed
        output_file_path = fr'{work_dir}\outputImg\{image_file_names[i]}{i}_no_face.png'
        bw_image.save(output_file_path)
