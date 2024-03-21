import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog

class Whiteboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Whiteboard")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.draw)

        self.menu = tk.Menu(self)
        self.configure(menu=self.menu)
        self.create_menu()

        self.current_color = "black"
        self.current_width = 2

    def create_menu(self):
        file_menu = tk.Menu(self.menu, tearoff=False)
        file_menu.add_command(label="Clear", command=self.clear_canvas)
        file_menu.add_command(label="Save", command=self.save_drawing)
        file_menu.add_command(label="Load", command=self.load_drawing)
        file_menu.add_command(label="Quit", command=self.quit)
        self.menu.add_cascade(label="File", menu=file_menu)

        color_menu = tk.Menu(self.menu, tearoff=False)
        color_menu.add_command(label="Choose Color", command=self.choose_color)
        self.menu.add_cascade(label="Color", menu=color_menu)

        thickness_menu = tk.Menu(self.menu, tearoff=False)
        thickness_menu.add_command(label="Thin", command=lambda: self.set_thickness(2))
        thickness_menu.add_command(label="Medium", command=lambda: self.set_thickness(5))
        thickness_menu.add_command(label="Thick", command=lambda: self.set_thickness(10))
        self.menu.add_cascade(label="Thickness", menu=thickness_menu)

    def draw(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color, width=self.current_width)

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.current_color = color

    def set_thickness(self, thickness):
        self.current_width = thickness

    def save_drawing(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            self.canvas.postscript(file=filename + ".eps", colormode='color')
            import PIL.Image
            img = PIL.Image.open(filename + ".eps")
            img.save(filename)

    def load_drawing(self):
        filename = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if filename:
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor="nw", image=tk.PhotoImage(file=filename))

if __name__ == "__main__":
    app = Whiteboard()
    app.mainloop()
