import cv2
import tkinter as tk
from PIL import Image, ImageTk

class SmileDetectorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Smile Detection")

        # Load Haar cascades
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)

        # GUI elements
        self.label = tk.Label(window)
        self.label.pack()

        self.message_var = tk.StringVar()
        self.message_label = tk.Label(window, textvariable=self.message_var, font=("Helvetica", 16))
        self.message_label.pack()

        # Start video update loop
        self.update_frame()

        # Close app cleanly
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            smiling = False
            for (x, y, w, h) in faces:
                face_roi = gray[y:y+h, x:x+w]
                
                # Lesser the sacleFactor for better detection of real-world smiles.
                smiles = self.smile_cascade.detectMultiScale(face_roi, scaleFactor=1.8, minNeighbors=20)

                if len(smiles) > 0:
                    smiling = True
                # Draw rectangle around face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            self.message_var.set("You are smiling : 😊" if smiling else "Not smiling :😑")

            # Convert to RGB and show in GUI
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)

        self.window.after(10, self.update_frame)

    def on_close(self):
        self.cap.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SmileDetectorApp(root)
    root.mainloop()
