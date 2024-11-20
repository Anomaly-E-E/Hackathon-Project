from pathlib import Path
from tkinter import  Canvas, Entry, Button, PhotoImage
import tkinter as tk
from tkinter import PhotoImage
import sqlite3
from tkinter import ttk
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/Arshan/Desktop/BRS/test/adminassets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def admin_login():
    
    password = entry_1.get()
    if password == "1234":
        data_window = tk.Toplevel()
        data_window.title("Admin Data Display")

        tree = ttk.Treeview(data_window, columns=("Name", "Destination","Address", "Phone Number","Email_ID","Weight", "Shipping Cost",'Tracking Number', 'Total cost'))
        tree.heading("#1", text="Name")
        tree.heading("#2", text="Destination (Emirates)")        
        tree.heading("#3", text="Address")
        tree.heading("#4", text="phone_Number")
        tree.heading("#5", text="email_id")
        tree.heading("#6", text="weight")
        tree.heading("#7", text="Shipping Cost")
        tree.heading("#8", text="Tracking Number")
        tree.heading("#9", text="Total Cost")
        
        conn = sqlite3.connect('ewaste.db')
        c = conn.cursor()
        c.execute("SELECT name, emirates, address, phone_Number, email_id, weight, shipping_cost, tracking_no, total_cost FROM collection")
        data = c.fetchall()

        for row in data:
            tree.insert('','9',values=row)

        conn.close()

        tree.pack()
    elif password == 'feedback':
        data_window = tk.Toplevel()
        data_window.title("Feedback Data Display")

        tree = ttk.Treeview(data_window, columns=("FEEDBACK"))
        tree.heading("#1", text="FEEDBACK")        
        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute("SELECT feedback_text TEXT FROM feedback")
        data = c.fetchall()

        for row in data:
            tree.insert('','1',values=row)

        conn.close()

        tree.pack()

window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("ADMIN LOGIN")

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
    106.0,
    700.0,
    501.0,
    fill="#6EA08E",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350.0,
    53.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    178.0,
    159.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    370.0,
    167.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    104.0,
    250.0,
    image=image_image_4
)

canvas.create_rectangle(
    0.0,
    278.0,
    291.0,
    343.0,
    fill="#6EA08E",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    150.5,
    307.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=41.0,
    y=288.0,
    width=219.0,
    height=36.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: admin_login(),
    relief="flat"
)
button_1.place(
    x=4.0,
    y=349.0,
    width=186.0,
    height=79.0
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
    x=640.0,
    y=446.0,
    width=60.0,
    height=54.0
)
window.resizable(False, False)
window.mainloop()
