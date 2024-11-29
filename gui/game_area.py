from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

from utils.board import Board

ASSETS_PATH = "assets/GameArea"

def relative_to_assets(path: str) -> Path:
    return Path(ASSETS_PATH) / Path(path)

class GameArea:
    def __init__(self, initial_player, mode="minimax", k_levels=4):
        self.canvas = None
        self.yellow_piece = None
        self.red_piece = None
        self.turn_indicator = None
        self.turn_flag = None
        self.score1 = None
        self.score2 = None
        self.board = Board(turn=initial_player, mode=mode)

    def update_gui(self):
        self.canvas.itemconfig(self.turn_indicator, text="Player " + str(self.board.get_player_turn()) + " ‘s turn")
        self.canvas.itemconfig(self.turn_flag, fill="#FF9D00" if self.board.get_player_turn() == 1 else "#D01466")
        player_1_score, player_2_score = self.board.get_scores()
        self.canvas.itemconfig(self.score1, text="Score: " + str(player_1_score))
        self.canvas.itemconfig(self.score2, text="Score: " + str(player_2_score))

    def draw_piece(self, col, row, player=None):
        if not player:
            return
        self.canvas.create_image(
            270 + 43 * col,
            185 + 43 * row,
            image=self.yellow_piece if player == 1 else self.red_piece,
        )
    
    def draw_board(self):
        for row in range(6):
            for col in range(7):
                self.draw_piece(col, row, self.board.get_cell(row, col))

    def insert_piece(self, col):
        is_added = self.board.add_piece(col)
        if not is_added:
            # TODO: display error message
            return
        self.draw_board()
        self.update_gui()
            
    def create_player_data(self, name, score, color, name_x, score_x, flag_x1, flag_x2, anchor="nw"):
        self.canvas.create_text(
            name_x,
            25.0,
            anchor=anchor,
            text=name,
            fill="#000000",
            font=("Inter Bold", 32 * -1)
        )
        score_text = self.canvas.create_text(
            score_x,
            71.0,
            anchor=anchor,
            text=f"Score: {score}",
            fill="#000000",
            font=("Inter Light", 13 * -1)
        )
        self.canvas.create_rectangle(
            flag_x1,
            25.0,
            flag_x2,
            87.0,
            fill=color,
            outline=""
        )
        return score_text

    def visualize(self):
        window = Tk()
        window.title("Game Area")
        window.geometry("800x500")
        window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.yellow_piece = PhotoImage(file=relative_to_assets("yellow.png"))
        self.red_piece = PhotoImage(file=relative_to_assets("red.png"))

        # background elements
        bg_shadow = PhotoImage(file=relative_to_assets("bg_shadow.png"))
        self.canvas.create_image(403.0, 446.0, image=bg_shadow)

        bottom_desk = PhotoImage(file=relative_to_assets("bottom_desk.png"))
        self.canvas.create_image(399.0, 434.0, image=bottom_desk)

        playing_desk = PhotoImage(file=relative_to_assets("playing_desk.png"))
        self.canvas.create_image(399.0, 294.0, image=playing_desk)

        # board base
        base = PhotoImage(file=relative_to_assets("base.png"))
        self.canvas.create_image(399, 292, image=base)
        
        
        # turn indicators
        self.turn_indicator = self.canvas.create_text(
            355.0,
            43.0,
            anchor="nw",
            text="Player " + str(self.board.get_player_turn()) + " ‘s turn",
            fill="#000000",
            font=("Inter", 13 * -1)
        )
        self.turn_flag = self.canvas.create_rectangle(
            355.0,
            65.0,
            446.0,
            71.0,
            fill="#FF9D00" if self.board.get_player_turn() == 1 else "#D01466",
            outline=""
        )

        # Player 1 data
        self.score1 = self.create_player_data(
            name="Player 1 (AI)",
            score=0,
            color="#FF9D00",
            name_x=53.0,
            score_x=53.0,
            flag_x1=0.0,
            flag_x2=43.0,
        )

        # Player 2 data
        self.score2 = self.create_player_data(
            name="Player 2",
            score=0,
            color="#D01466",
            name_x=747.0,
            score_x=688.0,
            flag_x1=757.0,
            flag_x2=800.0,
            anchor="ne"
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
                command=lambda i=i: self.insert_piece(i),
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

if __name__ == "__main__":
    game_area = GameArea(initial_player=2)
    game_area.visualize()