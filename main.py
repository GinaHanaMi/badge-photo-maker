import tkinter as tk
from tkinter import BOTTOM, LEFT, RIGHT, TOP, Button, Checkbutton, Entry, Frame, Label, Spinbox, StringVar, ttk, Menu, IntVar
from tkinter.filedialog import askopenfilenames, askdirectory

import os
import cv2
from PIL import Image, ImageTk
import numpy as np
from rembg import remove

class mainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Badge photo maker")
        
        self.monitor_width = root.winfo_screenwidth()
        self.monitor_height = root.winfo_screenheight()
        self.root.geometry(f"{self.monitor_width}x{self.monitor_height}")
        
        self.work_dir = os.getcwd()
        self.image_files = []
        self.displayed_image_index = 0
        self.saving_location = fr"{self.work_dir}\outputimg"
        

        self.before_image_frame = Frame(root)
        self.before_image_frame.pack(side=LEFT)
        self.before_image_label = Label(self.before_image_frame)
        self.before_image_label.pack(side=LEFT)
        
        self.after_image_frame = Frame(root)
        self.after_image_frame.pack(side=LEFT)
        self.after_image_label = Label(self.after_image_frame)
        self.after_image_label.pack(side=TOP)
        
        self.face_image_frame = Frame(self.after_image_frame)
        self.face_image_frame.pack(side=BOTTOM)
        self.face_image_label = Label(self.face_image_frame)
        
        
        self.middle_settings_frame = Frame(root, borderwidth=30)
        self.middle_settings_frame.pack(side=RIGHT)
        
        self.settings_label = Label(self.middle_settings_frame, text="SETTINGS")
        self.settings_label.grid(column=0, row=0, columnspan=2)
        
        self.automate_mode_var = IntVar()
        self.automate_mode = Checkbutton(self.middle_settings_frame, text="Automate", variable=self.automate_mode_var, onvalue=1, offvalue=0)
        self.automate_mode.grid(column=0, row=1, columnspan=2)
        
        self.black_and_white_var = IntVar()
        self.black_and_white_checkbox = Checkbutton(self.middle_settings_frame, text="Monochrome", variable=self.black_and_white_var, onvalue=1, offvalue=0)
        self.black_and_white_checkbox.grid(column=0, row=2, columnspan=2)
        
        self.detect_faces_checkbox_var = IntVar()
        self.detect_faces_checkbox = Checkbutton(self.middle_settings_frame, text="Detect faces", variable=self.detect_faces_checkbox_var, onvalue=1, offvalue=0)
        self.detect_faces_checkbox.grid(column=0, row=3, columnspan=2)
        

        self.detect_faces_ID_size_width_label = Label(self.middle_settings_frame ,text="Face width: ")
        self.detect_faces_ID_size_width_label.grid(column=0, row=4)
        self.detect_faces_ID_size_width_var = StringVar()
        self.detect_faces_ID_size_width = Entry(self.middle_settings_frame, textvariable=self.detect_faces_ID_size_width_var, width=9)
        self.detect_faces_ID_size_width.grid(column=1 ,row=4)
        self.detect_faces_ID_size_width.insert(0, "480")
        
        self.detect_faces_ID_size_height_label = Label(self.middle_settings_frame, text="Face height: ")
        self.detect_faces_ID_size_height_label.grid(column=0, row=5)
        self.detect_faces_ID_size_height_var = StringVar()
        self.detect_faces_ID_size_height = Entry(self.middle_settings_frame, textvariable=self.detect_faces_ID_size_height_var, width=9)
        self.detect_faces_ID_size_height.grid(column=1 ,row=5)
        self.detect_faces_ID_size_height.insert(0, "640")
        

        self.number_time_backround_removal_label = Label(self.middle_settings_frame, text="X of bg remove")
        self.number_time_backround_removal_label.grid(column=0, row=6)
        self.number_time_backround_removal_spinbox = Spinbox(self.middle_settings_frame, from_=0, to=10, width=7)
        self.number_time_backround_removal_spinbox.grid(column=1, row=6)
        
        self.submit_button = Button(self.middle_settings_frame, text="Submit", command=lambda: self.populate_after_image_frame(), width=9)
        self.submit_button.grid(column=0, row=7, columnspan=2)

        self.previous_image_button = Button(self.middle_settings_frame, text="Previous", command=self.previous_image, width=9)
        self.previous_image_button.grid(column=0, row=8)
        
        self.next_image_button = Button(self.middle_settings_frame, text="Next", command=self.next_image, width=9)
        self.next_image_button.grid(column=1, row=8)
        
        self.save_processed_checkbox_var = IntVar()
        self.save_processed_checkbox = Checkbutton(self.middle_settings_frame, text="Save processed?", variable=self.save_processed_checkbox_var, onvalue=1, offvalue=0)
        self.save_processed_checkbox.grid(column=0, row=9, columnspan=2)
        
        self.save_face_var = IntVar()
        self.save_face_checkbox = Checkbutton(self.middle_settings_frame, text="Save face?", variable=self.save_face_var, onvalue=1, offvalue=0)
        self.save_face_checkbox.grid(column=0, row=10, columnspan=2)
        
        self.save_images_button = Button(self.middle_settings_frame, text="Save", command=self.save_images_button, width=9)
        self.save_images_button.grid(column=0, row=11, columnspan=2)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        self.import_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        self.menu_bar.add_cascade(label="Import", menu=self.import_menu)
        self.import_menu.add_command(label="Import images", command=self.import_images)
        self.import_menu.add_command(label="Import all images from folder", command=self.import_images_from_folder)

    def import_images(self):
        image_paths_from_files = askopenfilenames(title="Select images", filetypes=[("All files", "*.*"), ("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if image_paths_from_files:
            for x in image_paths_from_files:
                self.image_files.append(x)
            self.populate_before_image_frame(self.displayed_image_index)

    def import_images_from_folder(self):
        folder_with_images_path = askdirectory(title="Select a folder with images")
        if folder_with_images_path:
            image_extensions = ['.png', '.jpg', '.jpeg', '.bmp']
            image_paths_from_folder = []
            for root, dirs, files in os.walk(folder_with_images_path):
                for file in files:
                    if os.path.splitext(file)[1].lower() in image_extensions:
                        image_paths_from_folder.append(os.path.join(root, file).replace('\\', '/'))
            for x in image_paths_from_folder:
                self.image_files.append(x)
            self.populate_before_image_frame(self.displayed_image_index)

    def populate_before_image_frame(self, displayed_image_index):
        if self.image_files:
            self.before_image_base = Image.open(self.image_files[displayed_image_index])
            self.before_image = self.before_image_base
            
            # Get the original dimensions of the image
            original_width, original_height = self.before_image_base.size
        
            self.space_between_images_in_percentage = 25
            
            # Define the maximum width and height of an image
            self.max_image_width = (self.monitor_width / 2) / 100 * (100-self.space_between_images_in_percentage)
            self.max_image_height = self.monitor_height / 100 * 90
        
            # Calculate the scaling factor to fit the image within the window while maintaining the aspect ratio
            self.image_scale = min(self.max_image_width / original_width, self.max_image_height / original_height)
        
            # Calculate the new dimensions
            self.new_image_width = int(original_width * self.image_scale)
            self.new_image_height = int(original_height * self.image_scale)
        
            # Resize the image
            self.before_image_base = self.before_image_base.resize((self.new_image_width, self.new_image_height), Image.LANCZOS)
            self.after_image = self.before_image_base

            self.before_image_ready = ImageTk.PhotoImage(image=self.before_image_base)

            self.before_image_label.config(image=self.before_image_ready)
            self.before_image_label.image = self.before_image_ready

    def populate_after_image_frame(self):
        self.after_image = self.before_image_base
        
        if self.black_and_white_var.get() == 1:
            self.after_image = self.after_image.convert("L")

        if int(self.number_time_backround_removal_spinbox.get()) > 0:
            for x in range(int(self.number_time_backround_removal_spinbox.get())):
                self.after_image = remove(self.after_image)
        
        self.save_processed_image = self.after_image

        if self.detect_faces_checkbox_var.get() == 1:
            self.face_image_label.pack(side=LEFT)
            
            self.id_photo_size = (int(self.detect_faces_ID_size_width_var.get()), int(self.detect_faces_ID_size_height_var.get()))

            haarcascade = fr"{self.work_dir}\haarcascade\haarcascade_frontalface_default.xml"
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            self.after_image = np.array(self.after_image)
            
            detected_faces = face_cascade.detectMultiScale(self.after_image, scaleFactor=1.05, minNeighbors=10, minSize=(100, 100))
            if len(detected_faces) > 0:
                x, y, w, h = detected_faces[0]
                
                # Defines the offset of that detection
                x -= int(0.15 * w) #0.1
                y -= int(0.3 * h) #0.2
                w += int(0.2 * w) #0.3
                h += int(0.8 * h) #0.5
                x = max(0, x)
                y = max(0, y)
                
                cropped_face = self.after_image[y:y + h, x:x + w].copy()

                # Convert numpy array back to PIL Image
                cropped_face_fromarray = Image.fromarray(cropped_face)
                
                # cropped_face_fromarray = cropped_face_fromarray.resize(self.id_photo_size)
                self.after_image_face = cropped_face_fromarray
                self.after_image_face = self.after_image_face.resize(self.id_photo_size)

                # Convert the final image to a PhotoImage object
                self.after_image_face_ready = ImageTk.PhotoImage(self.after_image_face)

                self.face_image_label.config(image=self.after_image_face_ready)
                self.face_image_label.image = self.after_image_face_ready
       
        else:
            self.face_image_label.forget()


        # Ensure after_image is a PIL Image before creating PhotoImage
        if isinstance(self.after_image, np.ndarray):
            self.after_image = Image.fromarray(self.after_image)

        self.after_image_ready = ImageTk.PhotoImage(self.after_image)
        self.after_image_label.config(image=self.after_image_ready)
        self.after_image_label.image = self.after_image_ready

                

                # output_file_path = fr'{work_dir}\outputImg\{image_file_names[i]}{i}_face1.png'
                # cropped_face_pil.save(output_file_path)
    

    def previous_image(self):
        if self.displayed_image_index > 0:
            self.displayed_image_index = self.displayed_image_index - 1
            
        self.populate_before_image_frame(self.displayed_image_index)

    def next_image(self):
        if self.displayed_image_index + 1 < len(self.image_files):
            self.displayed_image_index = self.displayed_image_index + 1
            
        self.populate_before_image_frame(self.displayed_image_index)

    def save_images_button(self):
        self.saving_location = askdirectory(title="Select a folder for images")
        
        if self.saving_location:
            if self.automate_mode_var.get() == 1:
                    for x, file in enumerate(self.image_files):
                        self.displayed_image_index = x
                        self.populate_before_image_frame(self.displayed_image_index)
                        self.populate_after_image_frame()

                        splitted = self.image_files[x].split("/")
                        
                        if self.save_face_var.get() == 1:
                            output_file_path = fr"{self.saving_location}\{splitted[-1]}_face.png"
                
                            if hasattr(self, 'after_image_face') and isinstance(self.after_image_face, Image.Image):
                                self.after_image_face.save(output_file_path)
                            
                        if self.save_processed_checkbox_var.get() == 1:
                            output_file_path = fr"{self.saving_location}\{splitted[-1]}_processed.png"
                            self.save_processed_image.save(output_file_path)
            else:
                self.populate_before_image_frame(self.displayed_image_index)
                self.populate_after_image_frame()

                if self.save_face_var.get() == 1:
                    splitted = self.image_files[self.displayed_image_index].split("/")
                    output_file_path = fr"{self.saving_location}\{splitted[-1]}_face_manual.png"
                    self.after_image_face.save(output_file_path)

                if self.save_processed_checkbox_var.get() == 1:
                    splitted = self.image_files[self.displayed_image_index].split("/")
                    output_file_path = fr"{self.saving_location}\{splitted[-1]}_processed_manual.png"
                    self.save_processed_image.save(output_file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = mainWindow(root)
    root.mainloop()