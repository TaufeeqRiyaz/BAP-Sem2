import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Viewer")
image_path = "pfp.png"
image = Image.open(image_path)

photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)

label.pack()
root.mainloop()