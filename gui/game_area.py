import math
import time

from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

from utils.board import Board
from algorithms.expected_minimax import ExpectedMinimax
from algorithms.minimax import Minimax
from gui.tree import MinimaxTree

ASSETS_PATH = "assets/GameArea"
MOVES = 21

def relative_to_assets(path: str) -> Path:
    return Path(ASSETS_PATH) / Path(path)

class GameArea:
    def __init__(self, initial_player, mode=0, k_levels=4):
        self.canvas = None
        self.window = None
        self.yellow_piece = None
        self.red_piece = None
        self.turn_indicator = None
        self.turn_flag = None
        self.score1 = None
        self.score2 = None
        self.mode = mode # 0 normal minimax, 1 alpha-beta, 2 expected minimax
        self.k_levels = k_levels # k is the depth of the minimax tree
        self.board = Board(7,6,initial_player, mode=self.mode) # 1 for player 1 (AI), 2 for player 2 (Human)
        self.last_tree = None
        self.total_time_for_agent = 0
        self.total_expanded_nodes = 0
        self.min_move_time = float(math.inf)
        self.max_move_time = float(-math.inf)


    def update_gui(self):
        self.canvas.itemconfig(self.turn_indicator, text="Player " + str(self.board.get_player_turn()) + " ‘s turn")
        self.canvas.itemconfig(self.turn_flag, fill="#FF9D00" if self.board.get_player_turn() == 1 else "#D01466")
        player_1_score, player_2_score = self.board.get_scores()
        self.canvas.itemconfig(self.score1, text="Score: " + str(player_1_score))
        self.canvas.itemconfig(self.score2, text="Score: " + str(player_2_score))
        print(self.board.get_heuristic_scores())

    def draw_piece(self, col, row, player=None):
        if player == 0:
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
        print("Add to column:", col)
        col, row = self.board.add_piece(col)
        if row == -1:
            print("Invalid move")
            return
        self.draw_piece(col, row, 2)
        self.update_gui()
        if self.board.is_terminal_node():
            self.end_game()
            return
        self.ai_move()
        self.update_gui()
        if self.board.is_terminal_node():
            self.end_game()
        
    def end_game(self):
        player1_score = self.board.player_1_actual_score
        player2_score = self.board.player_2_actual_score
        if player1_score > player2_score:
            winner = "Player 1"
        elif player2_score > player1_score:
            winner = "Player 2"
        else:
            winner = "It's a tie"
        
        print("--------------------------------------------------------------")
        print(f"Game over. {winner} wins!")
        print(f"Player 1 Score: {player1_score}")
        print(f"Player 2 Score: {player2_score}")
        print(f"Total number of node expanded: {self.total_expanded_nodes}")
        print(f"Total time taken by ai agent: {self.total_time_for_agent}")
        print(f"Avg. time taken by ai agent: {self.total_time_for_agent/MOVES}")
        print(f"Min. move time: {self.min_move_time}")
        print(f"Max. move time: {self.max_move_time}")
        print("--------------------------------------------------------------")
        self.window.destroy()

    def show_last_tree(self):
        if self.last_tree is None:
            print("No minimax tree to show.")
        else:
            self.last_tree.visualize()
            
    def ai_move(self):
        start_time = time.time()
        best_col = None
        row = None
        minimax_tree = None
        move_expanded_nodes = 0
        if self.mode == 0:
            minimax = Minimax(self.board, self.k_levels, self.board.get_player_turn() == 1)
            best_col, util, root = minimax.minimax_no_pruning()
            self.last_tree = MinimaxTree(self.k_levels,self.board.width,1,root)
            move_expanded_nodes += minimax.node_expanded
        elif self.mode == 1:
            minimax = Minimax(self.board, self.k_levels, self.board.get_player_turn() == 1)
            best_col, util, root = minimax.minimax_pruning()
            self.last_tree = MinimaxTree(self.k_levels,self.board.width,1,root)
            move_expanded_nodes += minimax.node_expanded
        elif self.mode == 2:
            expected_minimax = ExpectedMinimax(self.board, self.k_levels)
            best_col, util, root = expected_minimax.expected_minimax()
            self.last_tree = MinimaxTree(self.k_levels,self.board.width,2,root)
            move_expanded_nodes += expected_minimax.node_expanded

        print("AI Utility: ", util)
        print("AI Best Move: ", best_col)
        if best_col is not None:
            col, row = self.board.add_piece(best_col)
            self.draw_piece(col, row, 1)
            self.update_gui()

            if self.board.is_terminal_node():
                self.end_game()

        move_time = time.time() - start_time
        self.total_time_for_agent += move_time
        self.total_expanded_nodes += move_expanded_nodes
        self.min_move_time = min(self.min_move_time, move_time)
        self.max_move_time = max(self.max_move_time, move_time)
        print("Time taken: ", move_time)
        print("Node expanded: ", move_expanded_nodes)
        print("|------------------------------------|")

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
        self.window = window
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

        # Add button to show the last minimax tree
        show_tree_button = Button(
            window,
            text="Show Last Minimax Tree",
            anchor="center",
            command=self.show_last_tree,
            relief="flat"
        )
        show_tree_button.place(
            x=325,
            y=460,
            width=150,
            height=30
        )
    
        window.resizable(False, False)
        if(self.board.get_player_turn() == 1):
            self.ai_move()
        window.mainloop()


if __name__ == "__main__":
    game_area = GameArea(initial_player=2)
    game_area.visualize()
    
