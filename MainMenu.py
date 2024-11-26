

from pathlib import Path

from tkinter import Tk, Canvas, Button, PhotoImage, Entry


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\21011054\Fall 2024\AI\Lab 2\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Main Menu")

window.geometry("800x500")
window.configure(bg = "#FFFFFF")

def selectOption(option):
    global k
    ## option =1 for alph beta
    ## option =0 for no alpha beta
    if(entry_k.get() == ""):
        print("Enter a value for K")
        return
    k = int(entry_k.get())
    print(k)
    
    if(k>0):
        print(option)
        window.destroy()
    else:
        print("Enter a value for K")
        
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
    260.0,
    image=image_image_2
)

canvas.create_text(
    319.0,
    186.0,
    anchor="nw",
    text="Connect 4",
    fill="#000000",
    font=("Inter Bold", 32 * -1)
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
    x=339.0,
    y=240,
    width=123.0,
    height=28.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: selectOption(0),
    relief="flat"
)
button_2.place(
    x=339.0,
    y=279.0,
    width=123.0,
    height=28.0
)

## text area for the user to enter a variable K
k=-1
entry_k = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_k.place(
    x=389.0,
    y=315.0,
    width=70,
    height=20
)
text_1 = canvas.create_text(
    339.0,
    315.0,
    anchor="nw",
    text="K value: ",
    fill="#000000",
    font=("Inter Light", 13 * -1)
)


window.resizable(False, False)
window.mainloop()
