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

    def upload_image(self):
        # Logic for uploading image and performing facial recognition
        pass

    def live_recognition(self):
        # Logic for performing live facial recognition
        pass