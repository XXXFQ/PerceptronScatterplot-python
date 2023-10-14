import tkinter as tk

from .application import Application

def main():
    root = tk.Tk()
    root.geometry("900x500")
    root.minsize(width=900, height=500)
    app = Application(master=root)
    app.mainloop()

__all__ = [
    'main',
]