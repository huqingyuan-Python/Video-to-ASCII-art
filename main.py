import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
import threading

class VideoToAsciiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("视频转ASCII艺术")

        # Create a label for the canvas where ASCII art will be displayed
        self.ascii_label = tk.Label(root, text="Art Will Appear Here", font=('Courier', 10), justify='left')
        self.ascii_label.pack(pady=20)

        # Button to open file dialog and select video
        self.open_button = tk.Button(root, text="1.打开视频", command=self.load_video)
        self.open_button.pack(side=tk.LEFT, padx=10)

        # Button to start conversion
        self.start_button = tk.Button(root, text="2.开始转换", command=self.start_conversion)
        self.start_button.pack(side=tk.RIGHT, padx=10)

        self.video_path = None
        self.cap = None
        self.fps = 30  # Default FPS value
        self.running = False
        # Extended ASCII characters from darkest to lightest
        self.ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~i!lI;:,\"^`'. "
        self.frame_delay_ms = int(1000 / self.fps)  # Default delay based on default FPS

    def load_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if self.video_path:
            self.cap = cv2.VideoCapture(self.video_path)
            # Get the frames per second (FPS) of the video
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
            self.frame_delay_ms = int(1000 / self.fps)  # Update frame delay based on actual FPS

    def start_conversion(self):
        if not self.running and self.cap is not None:
            self.running = True
            threading.Thread(target=self.convert_to_ascii, daemon=True).start()

    def convert_to_ascii(self):
        while self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Resize image based on desired width
            width = 100  # Adjust this value for different output sizes
            height = int(gray_frame.shape[0] * (width / gray_frame.shape[1]))
            resized_image = cv2.resize(gray_frame, (width, height))

            # Normalize pixel values to range of ascii_chars
            normalized_image = np.interp(resized_image, (0, 255), (0, len(self.ascii_chars) - 1))
            ascii_art = "\n".join("".join(self.ascii_chars[int(pixel)] for pixel in row) for row in normalized_image)

            # Update the GUI with the new ASCII art
            self.update_ascii_display(ascii_art)

            # Wait for a moment to simulate real-time playback at the original video's FPS
            self.root.after(self.frame_delay_ms)  # Wait according to the calculated delay

        self.running = False
        self.cap.release()

    def update_ascii_display(self, ascii_art):
        self.ascii_label.config(text=ascii_art)
        self.root.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoToAsciiApp(root)
    root.mainloop()
