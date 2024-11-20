from pathlib import Path
import sys
from tkinter import Canvas, Entry ,Button, PhotoImage
import tkinter as tk
from tkinter import PhotoImage, messagebox
import sqlite3




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/Arshan/Desktop/BRS/test/feedbackassets/frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def store_feedback(): 
    feed=entry_1.get()
    conn_feedback = sqlite3.connect('feedback.db')
    c_feedback = conn_feedback.cursor()
    c_feedback.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            feedback_text VARCHAR
        )
    ''')
    conn_feedback.commit()
    c_feedback.execute("INSERT INTO feedback (feedback_text) VALUES (?)", (feed,))
    conn_feedback.commit()
    conn_feedback.close()
    
    messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")

window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("FEEDBACK")

window.geometry("700x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    126.0,
    0.0,
    700.0,
    500.0,
    fill="#6EA08E",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    63.0,
    250.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    255.0,
    76.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    404.0,
    145.0,
    image=image_image_3
)

canvas.create_rectangle(
    133.0,
    174.0,
    700.0,
    346.0,
    fill="#6EA08E",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    408.0,
    262.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=193.0,
    y=202.0,
    width=430.0,
    height=118.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: store_feedback(),
    relief="flat"
)
button_1.place(
    x=468.0,
    y=334.0,
    width=195.0,
    height=96.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sys.exit(),
    relief="flat"
)
button_2.place(
    x=126.0,
    y=444.0,
    width=60.0,
    height=54.0
)
window.resizable(False, False)
window.mainloop()
