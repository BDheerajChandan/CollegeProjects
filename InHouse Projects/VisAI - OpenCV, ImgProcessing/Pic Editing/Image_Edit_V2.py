import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import os
import mediapipe as mp

class ImageApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Live & Adjustable Image Viewer with Face + Hand Detection")
        self.window.state("zoomed")

        self.cap = cv2.VideoCapture(0)
        self.save_count = 0

        # Load OpenCV face detector
        haar_xml = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        if not os.path.exists(haar_xml):
            print("Haarcascade XML file not found!")
            self.window.destroy()
            return
        self.face_cascade = cv2.CascadeClassifier(haar_xml)

        # MediaPipe hand detection setup
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=2,
                                         min_detection_confidence=0.5,
                                         min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

        # Scrollable canvas setup
        self.canvas = tk.Canvas(self.window, borderwidth=0)
        self.vscrollbar = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vscrollbar.set)
        self.vscrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.main_frame = tk.Frame(self.canvas)
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        self.main_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.frame_width)

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Image 1 - Live feed with detection
        self.image1_frame = tk.Frame(self.main_frame)
        self.image1_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        tk.Label(self.image1_frame, text="Image 1 - Live Feed (Face + Hand Detection)", font=("Helvetica", 14, "bold")).pack()
        self.image1_label = tk.Label(self.image1_frame)
        self.image1_label.pack()

        self.width_label = tk.Label(self.image1_frame, font=("Helvetica", 10), anchor="w")
        self.width_label.pack(fill="x")
        self.height_label = tk.Label(self.image1_frame, font=("Helvetica", 10), anchor="w")
        self.height_label.pack(fill="x")
        self.channel_label = tk.Label(self.image1_frame, font=("Helvetica", 10), anchor="w")
        self.channel_label.pack(fill="x")
        self.brightness_label = tk.Label(self.image1_frame, font=("Helvetica", 10), anchor="w")
        self.brightness_label.pack(fill="x")
        self.contrast_label = tk.Label(self.image1_frame, font=("Helvetica", 10), anchor="w")
        self.contrast_label.pack(fill="x")
        self.hue_label = tk.Label(self.image1_frame, font=("Helvetica", 10), anchor="w")
        self.hue_label.pack(fill="x")
        self.saturation_label = tk.Label(self.image1_frame, font=("Helvetica", 10), anchor="w")
        self.saturation_label.pack(fill="x")

        # Image 2 - Mirror + adjustments
        self.image2_frame = tk.Frame(self.main_frame)
        self.image2_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        tk.Label(self.image2_frame, text="Image 2 - Mirror Adjusted", font=("Helvetica", 14, "bold")).pack()
        self.image2_label = tk.Label(self.image2_frame)
        self.image2_label.pack()

        self.build_controls(self.image2_frame)

        self.update_frame()
        self.window.protocol("WM_DELETE_WINDOW", self.stop)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def frame_width(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def build_controls(self, parent):
        control_frame = tk.Frame(parent)
        control_frame.pack(pady=10)

        def add_slider_row(label_text, from_, to, resolution=1, default_val=0):
            row = tk.Frame(control_frame)
            row.pack(fill="x", pady=2)
            lbl = tk.Label(row, text=f"{label_text} :", width=10, anchor='w')
            lbl.pack(side="left")
            scale = tk.Scale(row, from_=from_, to=to, resolution=resolution,
                             orient=tk.HORIZONTAL, length=200)
            scale.set(default_val)
            scale.pack(side="left")
            return scale

        self.brightness_scale = add_slider_row("Brightness", -100, 100, 1, 0)
        self.contrast_scale = add_slider_row("Contrast", 0.5, 3.0, 0.1, 1.0)
        self.hue_scale = add_slider_row("Hue", -180, 180, 1, 0)
        self.saturation_scale = add_slider_row("Saturation", 0.0, 3.0, 0.1, 1.0)

        btn_frame = tk.Frame(control_frame)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="LIVE", command=self.reset_controls).pack(side="left", padx=5)
        tk.Button(btn_frame, text="SAVE", command=self.save_image2).pack(side="left", padx=5)
        tk.Button(btn_frame, text="STOP", fg="red", command=self.stop).pack(side="left", padx=5)

    def reset_controls(self):
        self.brightness_scale.set(0)
        self.contrast_scale.set(1.0)
        self.hue_scale.set(0)
        self.saturation_scale.set(1.0)

    def apply_adjustments(self, frame):
        brightness = self.brightness_scale.get()
        contrast = self.contrast_scale.get()
        frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
        hue_shift = self.hue_scale.get()
        saturation = self.saturation_scale.get()

        hsv[..., 0] = (hsv[..., 0] + hue_shift) % 180
        hsv[..., 1] *= saturation
        hsv = np.clip(hsv, 0, 255)

        frame = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
        return frame

    def calculate_image_properties(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        brightness = int(np.mean(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)))
        contrast = np.std(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        hue = int(np.mean(hsv[..., 0]))
        saturation = int(np.mean(hsv[..., 1]))
        return brightness, contrast, hue, saturation

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
        return faces

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        display_size = (480, 360)

        # -------- Image 1 - Live with face and hand detection --------
        faces = self.detect_faces(frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        rgb_frame_for_hands = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame_for_hands)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized_rgb_frame = cv2.resize(rgb_frame, display_size)
        img1 = Image.fromarray(resized_rgb_frame)
        imgtk1 = ImageTk.PhotoImage(img1)
        self.image1_label.imgtk = imgtk1
        self.image1_label.config(image=imgtk1)

        height, width, channels = frame.shape
        self.width_label.config(text=f"Width: {width} px")
        self.height_label.config(text=f"Height: {height} px")
        self.channel_label.config(text=f"Channels: {channels}")

        b, c, h, s = self.calculate_image_properties(frame)
        self.brightness_label.config(text=f"Brightness: {b}")
        self.contrast_label.config(text=f"Contrast: {c:.2f}")
        self.hue_label.config(text=f"Hue: {h}")
        self.saturation_label.config(text=f"Saturation: {s}")

        # -------- Image 2 - Mirror + adjusted --------
        mirror = cv2.flip(frame, 1)
        mirror = self.apply_adjustments(mirror)
        self.last_adjusted_frame = mirror.copy()

        mirror_rgb = cv2.cvtColor(mirror, cv2.COLOR_BGR2RGB)
        resized_mirror = cv2.resize(mirror_rgb, display_size)
        img2 = Image.fromarray(resized_mirror)
        imgtk2 = ImageTk.PhotoImage(img2)
        self.image2_label.imgtk = imgtk2
        self.image2_label.config(image=imgtk2)

        self.window.after(10, self.update_frame)

    def save_image2(self):
        if hasattr(self, 'last_adjusted_frame'):
            self.save_count += 1
            filename = f"saved_image_{self.save_count}.png"
            cv2.imwrite(filename, self.last_adjusted_frame)
            print(f"Image saved as {filename}")
        else:
            print("No image to save yet.")

    def stop(self):
        self.cap.release()
        self.hands.close()
        self.window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
