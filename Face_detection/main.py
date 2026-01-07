import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading

class FaceEyeDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Face & Eye Detection GUI")
        self.root.geometry("800x600")
        
        # Load cascades
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        self.cap = None
        self.is_running = False
        
        self.setup_gui()
    
    def setup_gui(self):
        # Video frame
        self.video_label = tk.Label(self.root)
        self.video_label.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Ready - Click Start", font=("Arial", 12))
        self.status_label.pack()
        
        # Buttons frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        self.start_btn = tk.Button(btn_frame, text="Start Detection", command=self.start_detection, bg="green", fg="white")
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop_detection, bg="red", fg="white", state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        self.quit_btn = tk.Button(btn_frame, text="Quit", command=self.root.quit)
        self.quit_btn.pack(side=tk.LEFT, padx=5)
    
    def start_detection(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0)
        self.is_running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Detecting faces and eyes...")
        self.update_frame()
    
    def stop_detection(self):
        self.is_running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Stopped")
    
    def update_frame(self):
        if self.is_running:
            ret, frame = self.cap.read()
            if ret:
                # Detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
                
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                    
                    # Eye detection in face region
                    face_roi = gray[y:y+h, x:x+w]
                    eyes = self.eye_cascade.detectMultiScale(face_roi)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
                        cv2.putText(frame, 'Eye', (x+ex, y+ey-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Convert for Tkinter
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
            
            self.root.after(10, self.update_frame)
    
    def __del__(self):
        if self.cap:
            self.cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceEyeDetector(root)
    root.mainloop()
