from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Entry

ASSETS_PATH = "assets/MainMenu"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

k = -1
Ai = -1
startPlayer = -1


## function to select the option and start the game
## used after the button are clicked
## should return the values and start the game
def selectOption(window, entry_k ,entry_starter ,option):
    global k, Ai, startPlayer
    
    ## validation
    if (entry_k.get() == "" or entry_k.get().isnumeric() == False):
        print("Enter a value for K")
        return
    if (entry_starter.get() == "" or entry_starter.get().isnumeric() == False):
        print("Enter a value for Starting Player")
        return
    
    k = int(entry_k.get()) ## k is the depth of the minimax tree
    Ai = option ## 0 normal minimax, 1 alph beta, 2 expected minimax
    startPlayer = int(entry_starter.get()) ## 1 for player 1 (AI), 2 for player 2 (Human)
    
    ## value check
    if (k > 0 and startPlayer > 0 and startPlayer < 3):
        print("K: ", k)
        print("AI: ", Ai)
        print("Starting Player: ", startPlayer)
        window.destroy()
    else:
        print("Enter valid values for K and Starting Player")



def StartGui():
    
    window = Tk()
    window.title("Main Menu")
    window.geometry("800x500")
    window.configure(bg = "#FFFFFF")
    
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

    bg_image = PhotoImage(file=relative_to_assets("image_1.png"))
    bg_element = canvas.create_image(
        100.0,
        611.0,
        image=bg_image
    )

    ## background element animation
    def animate_image():
        x, y = canvas.coords(bg_element)
        if y > -100:
            canvas.move(bg_element, 0, -1)
            window.after(60, animate_image)

    animate_image()

    Menu_image = PhotoImage(file=relative_to_assets("image_2.png"))
    Menu = canvas.create_image(
        400.0,
        250.0,
        image=Menu_image
    )
    Title = canvas.create_text(
        319.0,
        137.0,
        anchor="nw",
        text="Connect 4",
        fill="#000000",
        font=("Inter Bold", 32 * -1)
    )

    Option_0_image = PhotoImage(file=relative_to_assets("button_0.png"))
    button_Option_0 = Button(
        image=Option_0_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: selectOption(window, entry_k ,entry_starter,0),
        relief="flat"
    )
    button_Option_0.place(
        x=335.0,
        y=193.0,
        width=130.0,
        height=30.0
    )

    Option_1_image = PhotoImage(file=relative_to_assets("button_1.png"))
    button_Option_1 = Button(
        image=Option_1_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: selectOption(window, entry_k ,entry_starter,1),
        relief="flat"
    )
    button_Option_1.place(
        x=335.0,
        y=233.0,
        width=130.0,
        height=30.0
    )

    Option_2_image = PhotoImage(file=relative_to_assets("button_2.png"))
    button_Option_2 = Button(
        image=Option_2_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: selectOption(window, entry_k ,entry_starter,2),
        relief="flat"
    )
    button_Option_2.place(
        x=335.0,
        y=273.0,
        width=130.0,
        height=30.0
    )

    ## text area for the user to enter a variable K
    entry_bg_1 = canvas.create_image(
        426.5,
        323.0,
        image=PhotoImage(file=relative_to_assets("entry_1.png"))
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
    text_k = canvas.create_text(
        335.0,
        315.0,
        anchor="nw",
        text="Enter K:",
        fill="#757575",
        font=("Inter", 12 * -1)
    )

    ## text area for the user to the starting player
    entry_bg_2 = canvas.create_image(
        426.5,
        353.0,
        image=PhotoImage(file=relative_to_assets("entry_2.png"))
    )
    entry_starter = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_starter.place(
        x=393.0,
        y=343.0,
        width=67.0,
        height=18.0
    )
    text_starter = canvas.create_text(
        335.0,
        345.0,
        anchor="nw",
        text="Starting:",
        fill="#757575",
        font=("Inter", 12 * -1)
    )
    window.resizable(False, False)
    window.mainloop()

StartGui()
