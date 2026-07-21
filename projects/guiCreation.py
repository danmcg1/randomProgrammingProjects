import tkinter as tk
root = tk.Tk()

# Setting some window properties
root.title("Tk Example")
root.minsize(1000, 1000)
root.maxsize(5000, 5000)
root.geometry("300x300+50+50")

tk.Label(root, text="Nothing will work unless you do.").pack()
tk.Label(root, text="- Maya Angelou").pack()



root.mainloop()
