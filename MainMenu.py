

from pathlib import Path

from tkinter import Tk, Canvas, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\21011054\Fall 2024\AI\Lab 2\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Main Menu")

window.geometry("800x500")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
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
    249.0,
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
    y=250.0,
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
    y=289.0,
    width=123.0,
    height=28.0
)

def selectOption(option):
    ## option =1 for alph beta
    ## option =0 for no alpha beta
    print(option)
    window.destroy()
    
window.resizable(False, False)
window.mainloop()
