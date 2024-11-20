from importlib.metadata import entry_points
from pathlib import Path
from tkinter import Canvas, Entry, Button, PhotoImage
import tkinter as tk
from tkinter import PhotoImage, messagebox
import sqlite3
import sys
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/Arshan/Desktop/BRS/test/trackassets/frame0")




def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def track_pickup():
    def display_tracking_info(data):
        tracking_info_window = tk.Toplevel()
        tracking_info_window.title("Tracking Information")
        tracking_info_window.geometry('300x100')
        
        labels = ["Name", "Destination (Emirates)", "Phone Number", "Email ID", "Weight", "Shipping Cost", "Tracking Number", "Total Cost"]
        for i, label_text in enumerate(labels):
            if data[1] == 'Abu Dhabi':
                label = tk.Label(tracking_info_window, text=f"TRACKING STATUS:\nARRIVAL WITHIN 1 WORKING DAY")
                label.pack()
                break
            elif data[1] == 'Dubai':
                label = tk.Label(tracking_info_window, text=f"TRACKING STATUS:\nARRIVAL WITHIN 2 WORKING DAYS")
                label.pack()
                break
            elif data[1] == 'Sharjah':
                label = tk.Label(tracking_info_window, text=f"TRACKING STATUS:\nARRIVAL WITHIN 3 WORKING DAYS")
                label.pack()
                break
            elif data[1] == 'Ajman':
                label = tk.Label(tracking_info_window, text=f"TRACKING STATUS:\nARRIVAL WITHIN 4 WORKING DAYS")
                label.pack()
                break
            elif data[1] == 'Umm Al-Quwain':
                label = tk.Label(tracking_info_window, text=f"TRACKING STATUS:\nARRIVAL WITHIN 5 WORKING DAYS")
                label.pack()
                break
            elif data[1] == 'Ras Al Khaimah':
                label = tk.Label(tracking_info_window, text=f"TRACKING STATUS:\nARRIVAL WITHIN 6 WORKING DAYS")
                label.pack()
                break
            else:
                label = tk.Label(tracking_info_window, text=f"TRACKING STATUS:\nARRIVAL WITHIN 7 WORKING DAYS")
                label.pack()
                break

   
    track_window = entry_1.get()
    if len(track_window) < 9 :
        conn = sqlite3.connect('ewaste.db')
        c = conn.cursor()
        sql = 'SELECT * FROM collection WHERE tracking_no = ?'
        392622        
        value = (track_window,)
        c.execute(sql, value)
        
        data = c.fetchone()
        conn.close()
        
        if data:
            display_tracking_info(data)
        else:
            messagebox.showerror("Error", "Tracking Number not found")
    else:
        conn = sqlite3.connect('ewaste.db')
        c = conn.cursor()
        sql = 'SELECT * FROM collection WHERE phone_Number = ?'
        
        value = (track_window,)
        c.execute(sql, value)
        
        data = c.fetchone()
        conn.close()
        
        if data:
            display_tracking_info(data)
        else:
            messagebox.showerror("Error", "Phone Number not found")
        


window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("TRACK")

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
    700.0,
    424.0,
    fill="#6EA08E",
    outline="")

canvas.create_rectangle(
    100.0,
    167.0,
    597.0,
    279.0,
    fill="#6EA08E",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    350.0,
    211.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=204.0,
    y=189.0,
    width=292.0,
    height=43.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    348.0,
    112.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    564.0,
    207.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    350.0,
    461.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: track_pickup(),
    relief="flat"
)
button_1.place(
    x=184.0,
    y=240.0,
    width=497.0,
    height=112.0
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
    x=0.0,
    y=369.0,
    width=60.0,
    height=54.0
)
window.resizable(False, False)
window.mainloop()
