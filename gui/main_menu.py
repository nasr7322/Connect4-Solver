from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Entry

from .game_area import GameArea

ASSETS_PATH = Path("assets/MainMenu")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainMenu:
    def __init__(self):
        self.window = None
        self.canvas = None
        self.entry_k = None
        self.entry_starter = None
        self.k = None
        self.Ai = None
        self.startPlayer = None

    def selectOption(self, option):
        ## validation
        if self.entry_k.get() == "" or not self.entry_k.get().isnumeric():
            print("Enter a value for K")
            return
        if self.entry_starter.get() == "" or not self.entry_starter.get().isnumeric():
            print("Enter a value for Starting Player")
            return

        self.k = int(self.entry_k.get())  # k is the depth of the minimax tree
        self.Ai = option  # 0 normal minimax, 1 alpha-beta, 2 expected minimax
        self.startPlayer = int(self.entry_starter.get())  # 1 for player 1 (AI), 2 for player 2 (Human)

        ## value check
        if self.k > 0 and 1 <= self.startPlayer <= 2:
            print("K: ", self.k)
            print("AI: ", self.Ai)
            print("Starting Player: ", self.startPlayer)
            self.window.destroy()
            game_area = GameArea(initial_player=self.startPlayer, mode=self.Ai, k_levels=self.k)
            game_area.visualize()

        else:
            print("Enter valid values for K and Starting Player")

    def animate_image(self, canvas, bg_element):
        x, y = canvas.coords(bg_element)
        if y > -100:
            canvas.move(bg_element, 0, -1)
            self.window.after(60, lambda: self.animate_image(canvas, bg_element))
        else:
            canvas.coords(bg_element, 100, 600)
            self.window.after(60, lambda: self.animate_image(canvas, bg_element))
            
    def create_entry_with_label(self, x, y, label_text):
        entry = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry.place(
            x=x + 60,
            y=y,
            width=67.0,
            height=18.0
        )
        self.canvas.create_text(
            x,
            y,
            anchor="nw",
            text=label_text,
            fill="#757575",
            font=("Inter", 12 * -1)
        )
        return entry

    def visualize(self):
        self.window = Tk()
        self.window.title("Main Menu")
        self.window.geometry("800x500")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#F0F0F0",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        ## Animating Backgound
        bg_image = PhotoImage(file=relative_to_assets("BG.png"))
        bg_element = self.canvas.create_image(100.0, 600.0, image=bg_image)
        self.animate_image(self.canvas, bg_element)

        ## menu board and title
        Menu_image = PhotoImage(file=relative_to_assets("Menu.png"))
        Menu = self.canvas.create_image(400.0, 250.0, image=Menu_image)
        Title = self.canvas.create_text(
            400.0,
            150.0,
            anchor="center",
            text="Connect 4",
            fill="#000000",
            font=("Inter Bold", 32 * -1)
        )

        ## buttons for the user to select the AI type
        for i in range(3):
            option_image = PhotoImage(file=relative_to_assets(f"button_{i}.png"))
            button_option = Button(
                image=option_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda i=i: self.selectOption(i),
                relief="flat"
            )
            button_option.image = option_image  # Keep a reference to the image to prevent garbage collection
            button_option.place(
                x=335.0,
                y=190.0 + (i * 40.0),
                width=130.0,
                height=30.0
            )

        ## text area for the user to enter a variable K
        self.entry_k = self.create_entry_with_label(335.0, 315.0, "Enter K:")

        ## text area for the user to the starting player
        self.entry_starter = self.create_entry_with_label(335.0, 345.0, "Starting:")
        
        self.window.resizable(False, False)
        self.window.mainloop()

if __name__ == "__main__":
  menu = MainMenu()
  menu.visualize()
