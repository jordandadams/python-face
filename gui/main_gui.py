import cv2
import tkinter.filedialog
from PIL import Image, ImageTk
import customtkinter as ctk

class FacialRecognitionGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Facial Recognition Testing")
        self.geometry(f"{800}x{800}")

        # Heading
        self.heading_label = ctk.CTkLabel(self, text="Facial Recognition Testing", font=ctk.CTkFont(size=24, weight="bold"))
        self.heading_label.pack(pady=(20, 40))

        # Upload Image Button
        self.upload_image_button = ctk.CTkButton(self, text="Upload Image", command=self.upload_image)
        self.upload_image_button.pack(pady=10)

        # LIVE Recognition Button
        self.live_recognition_button = ctk.CTkButton(self, text="LIVE Recognition", command=self.live_recognition)
        self.live_recognition_button.pack(pady=10)

        # Progress Bar
        self.progressbar = ctk.CTkProgressBar(self, mode="determinate")
        self.progressbar.pack(pady=10)
        self.progressbar.pack_forget()

        # Label to display the processed image
        self.image_canvas = ctk.CTkCanvas(self, width=800, height=600)
        self.image_canvas.pack(pady=10)
        self.image_canvas.pack_forget()

    def upload_image(self):
        # Open a file dialog to select an image
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if not file_path:
            return

        # Show the progress bar
        self.progressbar.pack()
        self.progressbar.set(0)
        print('progress started')

        # Schedule the processing part to run after a short delay (100 ms)
        self.after(100, lambda: self.process_image(file_path))

    def process_image(self, file_path):
        # Load the image using OpenCV
        image = cv2.imread(file_path)
        self.progressbar.set(0.2)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.progressbar.set(0.4)

        # Load pre-trained face detector
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        self.progressbar.set(0.6)

        # Draw rectangles around the faces
        self.image_canvas.delete("all")
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = image[y:y+h, x:x+w]
            self.image_canvas.create_rectangle(x, y, x+w, y+h, outline="", tags=("face",))

            def on_face_click(event, face):
                self.open_face_dialog(event, face)

            self.image_canvas.tag_bind("face", "<Button-1>", lambda event, f=face: on_face_click(event, f))

        self.progressbar.set(0.8)

        # Stop the progress bar
        self.progressbar.set(1)
        self.progressbar.pack_forget()

        # Convert the image to RGB format and display it in the label
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.image_canvas.create_image(0, 0, anchor="nw", image=image)
        self.image_canvas.image = image
        self.image_canvas.pack()


    def open_face_dialog(self, event, face):
        # Convert the face image to RGB format
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        # Convert face image to PIL format
        face = Image.fromarray(face)
        face = ImageTk.PhotoImage(face)
        # Open the FaceDialog window with the selected face
        FaceDialog(self, face)

    def live_recognition(self):
        # Logic for performing live facial recognition
        pass

class FaceDialog(ctk.CTkToplevel):
    def __init__(self, master, face_image):
        super().__init__(master)

        self.title("Save Face Information")
        self.geometry("400x400")

        # Create input fields for name, age, and address
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=10)
        self.age_entry = ctk.CTkEntry(self)
        self.age_entry.pack(pady=10)
        self.address_entry = ctk.CTkEntry(self)
        self.address_entry.pack(pady=10)

        # Create a save button
        self.save_button = ctk.CTkButton(self, text="Save", command=self.save_face)
        self.save_button.pack(pady=10)

        # Store the face image
        self.face_image = face_image

    def save_face(self):
        # Get the name, age, and address from the input fields
        name = self.name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()

        # Save the face image and information (for example, to a file or database)
        # The specific implementation depends on how you want to store the data
        # ...

        # Close the dialog
        self.destroy()