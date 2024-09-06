from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import Canvas
import main
import models

from PIL import ImageDraw, Image, ImageTk, ImageOps


class tk_window:
    def __init__(self):
        self.root=Tk()
        self.root.title("Digit recognition")
        self.root.geometry("950x650")
        self.root.configure(background="white")

        self.label =Label(self.root, text="Please draw a digit to be predicted", font=("Helvetica", 16), background="white").pack(side=TOP)

        self.canvas = Canvas(self.root, width=280, height=280, bg="black")
        self.canvas.pack()

        self.button_frame = Frame(self.root)
        self.button_frame.pack()

        self.upload_frame = Frame(self.root)
        self.upload_frame.pack(side=BOTTOM)

        self.clear_button = Button(self.button_frame, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=LEFT)

        self.submit_button = Button(self.button_frame, text="Predict", command=self.submit_image)
        self.submit_button.pack(side=LEFT)

        self.submit_image_button = Button(self.upload_frame, text="Predict", command=self.submit_uploaded_image)
        self.submit_image_button.pack(side=BOTTOM)

        self.image_uploader = Button(self.upload_frame, text="Locate Image", command=self.image_upload)
        self.image_uploader .pack(side=BOTTOM)



        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.image = Image.new("L", (280, 280), 0)
        self.draw = ImageDraw.Draw(self.image)
        self.last_x, self.last_y = None, None

    def start_drawing(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.last_x and self.last_y:
            x, y = event.x, event.y
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="white", width=8)
            self.draw.line([self.last_x, self.last_y, x, y], fill="white", width=8)
            self.last_x, self.last_y = x, y

    def stop_drawing(self, event):
        self.last_x, self.last_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (280, 280), 0)
        self.draw = ImageDraw.Draw(self.image)

    def submit_image(self):
        self.image.save("digit.png")
        result =main.predict("digit.png")

        messagebox.showinfo("Result", f"The digit is predicted to be {result}")

    def image_upload(self):
        fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
        path = filedialog.askopenfilename(filetypes=fileTypes)

        if len(path):
            img = Image.open(path)
            img = img.resize((280, 280))
            pic=img.convert('L')
            pic = ImageOps.invert(pic)

            pic.save("digit.png")
            messagebox.showinfo(title="Successfull Upload", message=f"The file was uplaoded click predict ")

        else :
            messagebox.showinfo("Error", f"The file was not uploaded please upload correctly")

    def submit_uploaded_image(self):
        result = main.predict("digit.png")

        messagebox.showinfo("Result", f"The digit is predicted to be {result}")


    def run_window(self):
        self.root.mainloop()

if __name__ == "__main__":
    p=tk_window()
    p.run_window()


