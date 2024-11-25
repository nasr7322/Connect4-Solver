
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\21011054\Fall 2024\AI\Lab 2\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Game Area")
Player = 1 ## innitial player - change if u want ai to start first
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

## background elements
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    403.0,
    446.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    399.0,
    434.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    399.0,
    294.0,
    image=image_image_3
)

## board base
image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    399,
    292,
    image=image_image_4
)

yellowPiece = PhotoImage(
    file=relative_to_assets("image_5.png"))
redPiece = PhotoImage(
    file=relative_to_assets("image_6.png"))

##Plater names
canvas.create_text(
    53.0,
    25.0,
    anchor="nw",
    text="Player 1",
    fill="#000000",
    font=("Inter Bold", 32 * -1)
)
canvas.create_text(
    747.0,
    25.0,
    anchor="ne",
    text="Player 2 (AI)",
    fill="#000000",
    font=("Inter Bold", 32 * -1)
)

## turn indicator
turn_indicator = canvas.create_text(
    355.0,
    43.0,
    anchor="nw",
    text="Player " + str(Player) + " ‘s turn",
    fill="#000000",
    font=("Inter", 13 * -1)
)
## color flag indicator
flag = canvas.create_rectangle(
    355.0,
    65.0,
    446.0,
    71.0,
    fill="#FF9D00" if Player == 1 else "#D01466",
    outline="")

##player 1's score flag
canvas.create_text(
    53.0,
    71.0,
    anchor="nw",
    text="Score: 00",
    fill="#000000",
    font=("Inter Light", 13 * -1)
)
##player 2's score flag
canvas.create_text(
    688.0,
    71.0,
    anchor="nw",
    text="Score: 00",
    fill="#000000",
    font=("Inter Light", 13 * -1)
)

##player 2's color flag
canvas.create_rectangle(
    757.0,
    25.0,
    800.0,
    87.0,
    fill="#D01466",
    outline="")
##player 1's color flag
canvas.create_rectangle(
    0.0,
    25.0,
    43.0,
    87.0,
    fill="#FF9D00",
    outline="")

def insertPiece(Col, Row=5):
    global Player
    canvas.create_image(
        270+43*Col,
        400-43*Row,
        image=yellowPiece if Player == 1 else redPiece,
    )
    Player = 2 if Player == 1 else 1
    canvas.itemconfig(turn_indicator, text="Player " + str(Player) + " ‘s turn")
    canvas.itemconfig(flag, fill="#FF9D00" if Player == 1 else "#D01466")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insertPiece(0),
    relief="flat"
)
button_1.place(
    x=255.0,
    y=114.0,
    width=28.0,
    height=28.000001907348633
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insertPiece(1),
    relief="flat"
)
button_2.place(
    x=298.0,
    y=114.0,
    width=28.0,
    height=28.000001907348633
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insertPiece(2),
    relief="flat"
)
button_3.place(
    x=341.0,
    y=114.0,
    width=28.0,
    height=28.000001907348633
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insertPiece(3),
    relief="flat"
)
button_4.place(
    x=384.0,
    y=114.0,
    width=28.0,
    height=28.000001907348633
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insertPiece(4),
    relief="flat"
)
button_5.place(
    x=427.0,
    y=114.0,
    width=28.0,
    height=28.000001907348633
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insertPiece(5),
    relief="flat"
)
button_6.place(
    x=470.0,
    y=114.0,
    width=28.0,
    height=28.000001907348633
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insertPiece(6),
    relief="flat"
)
button_7.place(
    x=513.0,
    y=114.0,
    width=28.0,
    height=28.000001907348633
)

window.resizable(False, False)
window.mainloop()
