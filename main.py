import os
from gc import collect
from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
from tkinter import * 
import  tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/Arshan/Desktop/BRS/test/mainassets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("ECOWAY")


window.geometry("700x500")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=500,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    220.0,
    500.0,
    fill="#1A2229",
    outline=""
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image1.png")
)
image_1 = canvas.create_image(
    150.0,
    350.0,
    image=image_image_1
)

canvas.create_rectangle(
    220.0,
    0.0,
    700.0,
    500.0,
    fill="#6EA08E",
    outline=""
)

canvas.create_rectangle(
    319.0,
    285.0,
    579.0,
    329.0,
    fill="#6EA08E",
    outline=""
)

canvas.create_rectangle(
    321.0,
    377.0,
    581.0,
    421.0,
    fill="#6EA08E",
    outline=""
)

canvas.create_rectangle(
    321.0,
    200.0,
    581.0,
    244.0,
    fill="#6EA08E",
    outline=""
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image2.png")
)
image_2 = canvas.create_image(
    619.0,
    310.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image3.png")
)
image_3 = canvas.create_image(
    619.0,
    220.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image4.png")
)
image_4 = canvas.create_image(
    616.0,
    403.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button1.png")
)
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python3 admin.py'),
    relief="flat"
)
button_1.place(
    x=220.0,
    y=439.0,
    width=162.0,
    height=173.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button2.png")
)
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python3 about.py'),
    relief="flat"
)
button_2.place(
    x=628.0,
    y=453.0,
    width=103.0,
    height=94.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button3.png")
)
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python3 feedback.py'),
    relief="flat"
)
button_3.place(
    x=326.0,
    y=374.0,
    width=250.0,
    height=51.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button4.png")
)
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python3 track.py'),
    relief="flat"
)
button_4.place(
    x=326.0,
    y=282.0,
    width=250.0,
    height=51.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button5.png")
)
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: os.system('python3 apply.py'),
    relief="flat"
)
button_5.place(
    x=326.0,
    y=196.0,
    width=250.0,
    height=51.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image5.png")
)
image_5 = canvas.create_image(
    460.0,
    106.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()