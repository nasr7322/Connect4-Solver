from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Entry

ASSETS_PATH = "assets/MainMenu"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Main Menu")
window.geometry("800x500")
window.configure(bg = "#FFFFFF")

k = -1
Ai = -1
startPlayer = -1

def selectOption(option):
    global k, Ai, startPlayer
    if (entry_k.get() == "" or entry_k.get().isnumeric() == False):
        print("Enter a value for K")
        return
    if (starter.get() == "" or starter.get().isnumeric() == False):
        print("Enter a value for Starting Player")
        return
    
    k = int(entry_k.get())
    ## k is the depth of the minimax tree
    
    Ai = option
    ## option =0 for normal minimax
    ## option =1 for alph beta
    ## option =2 for Expected Minimax

    startPlayer = int(starter.get())
    ## startPlayer = 1 for player 1 (AI)
    ## startPlayer = 2 for player 2 (Human)
    
    if (k > 0 and startPlayer > 0 and startPlayer < 3):
        print("K: ", k)
        print("AI: ", Ai)
        print("Starting Player: ", startPlayer)
        window.destroy()
    else:
        print("Enter valid values for K and Starting Player")
        
canvas = Canvas(
    window,
    bg = "#F0F0F0",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    100.0,
    611.0,
    image=image_image_1
)
def animate_image():
    x, y = canvas.coords(image_1)
    if y > -100:
        canvas.move(image_1, 0, -1)
        window.after(60, animate_image)

animate_image()

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    400.0,
    250.0,
    image=image_image_2
)

canvas.create_text(
    319.0,
    137.0,
    anchor="nw",
    text="Connect 4",
    fill="#000000",
    font=("Inter Bold", 32 * -1)
)

button_image_0 = PhotoImage(
    file=relative_to_assets("button_0.png"))
button_0 = Button(
    image=button_image_0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selectOption(0),
    relief="flat"
)
button_0.place(
    x=335.0,
    y=193.0,
    width=130.0,
    height=30.0
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selectOption(1),
    relief="flat"
)
button_1.place(
    x=335.0,
    y=233.0,
    width=130.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selectOption(2),
    relief="flat"
)
button_2.place(
    x=335.0,
    y=273.0,
    width=130.0,
    height=30.0
)

## text area for the user to enter a variable K
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    426.5,
    323.0,
    image=entry_image_1
)
entry_k = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_k.place(
    x=393.0,
    y=313.0,
    width=67.0,
    height=18.0
)
text_1 = canvas.create_text(
    335.0,
    315.0,
    anchor="nw",
    text="Enter K:",
    fill="#757575",
    font=("Inter", 12 * -1)
)

## text area for the user to the starting player
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    426.5,
    353.0,
    image=entry_image_2
)
starter = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
starter.place(
    x=393.0,
    y=343.0,
    width=67.0,
    height=18.0
)
text_2 = canvas.create_text(
    335.0,
    345.0,
    anchor="nw",
    text="Starting:",
    fill="#757575",
    font=("Inter", 12 * -1)
)

window.resizable(False, False)
window.mainloop()
