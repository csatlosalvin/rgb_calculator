import tkinter as tk
import colorsys

class RGBCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("RGB Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#202124")
        
        self.equation = tk.StringVar()
        self.create_widgets()
        self.current_hue = 0
        self.update_colors()

    def create_widgets(self):
        # Display
        self.display = tk.Entry(self.root, textvariable=self.equation, font=('Segoe UI', 20), bd=10, insertwidth=4, width=14, borderwidth=0, bg="#303134", fg="#ffffff", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            'DEL'
        ]

        row, col = 1, 0
        self.button_widgets = []
        for button in buttons:
            btn = self.create_button(button, row, col)
            self.button_widgets.append(btn)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Configure grid layout
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i % 4, weight=1)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Segoe UI', 18, 'bold'), command=lambda: self.on_button_click(text), bg="#303134", fg="#ffffff", bd=1, relief="solid", activebackground="#404245", activeforeground="#ffffff")
        button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        return button

    def on_button_click(self, char):
        if char == 'C':
            self.equation.set("")
        elif char == 'DEL':
            current_text = self.equation.get()
            new_text = current_text[:-1]  # Remove the last character
            self.equation.set(new_text)
        elif char == '=':
            try:
                result = str(eval(self.equation.get()))
                self.equation.set(result)
            except:
                self.equation.set("ERROR")
        else:
            current_text = self.equation.get()
            new_text = current_text + str(char)
            self.equation.set(new_text)

    def update_colors(self):
        for widget in self.button_widgets:
            color = self.hsv_to_rgb(self.current_hue, 1, 1)
            widget.config(bg=color)
            self.current_hue += 0.001  # Smaller increment to slow down the color change
            if self.current_hue > 1:
                self.current_hue = 0
        self.root.after(50, self.update_colors)  # Increase the interval to slow down the update rate

    def hsv_to_rgb(self, h, s, v):
        rgb = colorsys.hsv_to_rgb(h, s, v)
        return f'#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}'

if __name__ == "__main__":
    root = tk.Tk()
    calculator = RGBCalculator(root)
    root.mainloop()
