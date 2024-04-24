import tkinter as tk
from PIL import Image, ImageTk

class CookieClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cookie Clicker")

        self.cookies = 0

        self.cookie_image = Image.open("cookie.jpg")
        self.cookie_image = ImageTk.PhotoImage(self.cookie_image)

        self.cookie_button = tk.Button(master, image=self.cookie_image, command=self.click_cookie)
        self.cookie_button.pack()

        self.counter_label = tk.Label(master, text="Cookies: 0")
        self.counter_label.pack()

    def click_cookie(self):
        self.cookies += 1
        self.counter_label.config(text=f"Cookies: {self.cookies}")

def main():
    root = tk.Tk()
    app = CookieClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
