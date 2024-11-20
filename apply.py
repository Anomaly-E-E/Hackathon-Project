from importlib.metadata import entry_points
from pathlib import Path
import tkinter as tk
from tkinter import PhotoImage, messagebox 
import sqlite3
import random
import sys
from tkinter import Canvas, Entry, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/Arshan/Desktop/BRS/test/applyassets/frame0")
conn = sqlite3.connect('ewaste.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS collection (
        name VARCHAR,
        emirates VARCHAR,
        address VARCHAR,
        phone_Number INTEGER,
        email_id VARCHAR,
        weight FLOAT,
        shipping_cost FLOAT,
        tracking_no INTEGER,
        total_cost FLOAT
    )
''')
conn.commit()
conn.close()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def append_text():
    name = ""
    emirates = ""
    address = ""
    phone_Number = ""
    email_id = ""
    weight = ""
    shipping_cost = ""
    tracking_no = ""
    total_cost = ""

    name = entry_2.get()
    weight = float(entry_5.get())
    emirates = entry_3.get()
    address = entry_1.get()
    distance = {"Abu Dhabi": 0, "Dubai": 6, "Sharjah": 7, "Ajman": 8, "Umm Al-Quwain": 9, "Ras Al Khaimah": 10, "Fujairah": 12}
    shipping_cost = distance[emirates.title()]
    phone_Number = int(entry_6.get())
    email_id = entry_4.get()
    n=random.randrange(10000,1000000)

    total_price = weight * 5 - shipping_cost
        
    conn = sqlite3.connect('ewaste.db')
    c = conn.cursor()
    c.execute("INSERT INTO collection (name, emirates, address, phone_Number, email_id, weight, shipping_cost, tracking_no, total_cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                 (name, emirates, address, phone_Number, email_id, weight, shipping_cost, n, total_price))
    conn.commit()
    conn.close()
    messagebox.showinfo("Cost Calculation", f"Total Cost: AED {total_price:.2f}")
    messagebox.showinfo('Tracking Number',f"Tracking Number: {n}" )


window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("APPLY FOR COLLECTION")

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
    0.0,
    0.0,
    575.0,
    500.0,
    fill="#6EA08E",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: append_text(),
    relief="flat"
)
button_1.place(
    x=398.0,
    y=435.0,
    width=170.0,
    height=77.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    288.0,
    44.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    109.0,
    407.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    109.0,
    350.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    109.0,
    293.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    109.0,
    236.0,
    image=image_image_5
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=140.0,
    width=222.0,
    height=78.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sys.exit(),
    relief="flat"
)
button_3.place(
    x=0.0,
    y=446.0,
    width=60.0,
    height=54.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    109.0,
    122.0,
    image=image_image_6
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    364.0,
    236.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=254.0,
    y=221.0,
    width=220.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    364.0,
    122.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=254.0,
    y=107.0,
    width=220.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    364.0,
    179.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=254.0,
    y=164.0,
    width=220.0,
    height=28.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    364.0,
    350.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=254.0,
    y=335.0,
    width=220.0,
    height=28.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    364.0,
    406.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=254.0,
    y=391.0,
    width=220.0,
    height=28.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    364.0,
    293.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=254.0,
    y=278.0,
    width=220.0,
    height=28.0
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    637.0,
    250.0,
    image=image_image_7
)
window.resizable(False, False)
window.mainloop()
