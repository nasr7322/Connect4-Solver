from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

ASSETS_PATH = "assets/GameArea"
def relative_to_assets(path: str) -> Path:
    return Path(ASSETS_PATH) / Path(path)

canvas = None
yellowPiece = None
redPiece = None
player = None

def updateGui(p, s1, s2):  # updates player's turn and scores
    canvas.itemconfig(turn_indicator, text="Player " + str(p) + " ‘s turn")
    canvas.itemconfig(turn_flag, fill="#FF9D00" if p == 1 else "#D01466")
    canvas.itemconfig(score1, text="Score: " + str(s1))
    canvas.itemconfig(score2, text="Score: " + str(s2))

def drawPiece(col, row, p):  # draws the piece on the board
    global canvas, yellowPiece, redPiece
    canvas.create_image(
        270 + 43 * col,
        400 - 43 * row,
        image=yellowPiece if p == 1 else redPiece,
    )

def insertPiece(col):
    global player
    # calculate row to insert (todo)
    row = 2
    # calculate score
    s1 = 0
    s2 = 0
    drawPiece(col, row, player)
    # go to next turn
    player = 2 if player == 1 else 1
    updateGui(player, s1, s2)

def StartGui(initialPlayer):
    global canvas, yellowPiece, redPiece, turn_indicator, turn_flag, score1, score2, player
    player = initialPlayer
    s1 = 0
    s2 = 0

    window = Tk()
    window.title("Game Area")
    window.geometry("800x500")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=500,
        width=800,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    yellowPiece = PhotoImage(file=relative_to_assets("image_5.png"))
    redPiece = PhotoImage(file=relative_to_assets("image_6.png"))

    # background elements
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        403.0,
        446.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        399.0,
        434.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        399.0,
        294.0,
        image=image_image_3
    )

    # board base
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        399,
        292,
        image=image_image_4
    )

    # Player names
    canvas.create_text(
        53.0,
        25.0,
        anchor="nw",
        text="Player 1 (AI)",
        fill="#000000",
        font=("Inter Bold", 32 * -1)
    )
    canvas.create_text(
        747.0,
        25.0,
        anchor="ne",
        text="Player 2",
        fill="#000000",
        font=("Inter Bold", 32 * -1)
    )
    # turn indicator
    turn_indicator = canvas.create_text(
        355.0,
        43.0,
        anchor="nw",
        text="Player " + str(player) + " ‘s turn",
        fill="#000000",
        font=("Inter", 13 * -1)
    )
    # color flag indicator
    turn_flag = canvas.create_rectangle(
        355.0,
        65.0,
        446.0,
        71.0,
        fill="#FF9D00" if player == 1 else "#D01466",
        outline=""
    )
    # player 1's score flag
    score1 = canvas.create_text(
        53.0,
        71.0,
        anchor="nw",
        text="Score: 0",
        fill="#000000",
        font=("Inter Light", 13 * -1)
    )
    # player 2's score flag
    score2 = canvas.create_text(
        688.0,
        71.0,
        anchor="nw",
        text="Score: 0",
        fill="#000000",
        font=("Inter Light", 13 * -1)
    )
    # player 2's color flag
    flag_1 = canvas.create_rectangle(
        757.0,
        25.0,
        800.0,
        87.0,
        fill="#D01466",
        outline=""
    )
    # player 1's color flag
    flag_2 = canvas.create_rectangle(
        0.0,
        25.0,
        43.0,
        87.0,
        fill="#FF9D00",
        outline=""
    )

    button_image = PhotoImage(file=relative_to_assets("button.png"))
    # Coordinates for the buttons
    x_start = 255.0
    y_coord = 114.0
    width = 28.0
    height = 28.0
    x_increment = 43.0
    buttons = []
    for i in range(7):
        button = Button(
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda i=i: insertPiece(i),
            relief="flat"
        )
        button.place(
            x=x_start + i * x_increment,
            y=y_coord,
            width=width,
            height=height
        )
        buttons.append(button)

    window.resizable(False, False)
    window.mainloop()

StartGui(2)