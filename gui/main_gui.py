import cv2
import tkinter.filedialog
from PIL import Image, ImageTk
import customtkinter

class FacialRecognitionGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Facial Recognition Testing")
        self.geometry(f"{800}x{800}")

        # Heading
        self.heading_label = customtkinter.CTkLabel(self, text="Facial Recognition Testing", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.heading_label.pack(pady=(20, 40))

        # Upload Image Button
        self.upload_image_button = customtkinter.CTkButton(self, text="Upload Image", command=self.upload_image)
        self.upload_image_button.pack(pady=10)

        # LIVE Recognition Button
        self.live_recognition_button = customtkinter.CTkButton(self, text="LIVE Recognition", command=self.live_recognition)
        self.live_recognition_button.pack(pady=10)

        # Progress Bar
        self.progressbar = customtkinter.CTkProgressBar(self, mode="determinate")
        self.progressbar.pack(pady=10)
        self.progressbar.pack_forget()

        # Label to display the processed image
        self.image_label = customtkinter.CTkLabel(self, text="")
        self.image_label.pack(pady=10)
        self.image_label.pack_forget()

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
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        self.progressbar.set(0.8)

        # Stop the progress bar
        self.progressbar.set(1)
        self.progressbar.pack_forget()

        # Convert the image to RGB format and display it in the label
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=image)
        self.image_label.image = image
        self.image_label.pack()

    def live_recognition(self):
        # Logic for performing live facial recognition
        pass