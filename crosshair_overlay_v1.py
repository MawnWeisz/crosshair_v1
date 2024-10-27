import tkinter as tk
from PIL import Image, ImageTk
import ctypes

def display_image(image_path):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.configure(bg='black')
    root.wm_attributes('-transparentcolor', 'black')
    root.config(cursor="none") 

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo, bg='black')
    label.image = photo  
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.bind('<Escape>', lambda e: root.destroy())

    root.update_idletasks()
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x80000 | 0x20)

    root.mainloop()

if __name__ == "__main__":
    image_path = "Crosshair.png" 
    display_image(image_path)