## Main file for the program
from gui.MainMenu import MainMenu
def main():
    # Start the main menu and return the values of K, Ai, and startPlayer
    # start the game loop with given values
    # each time a player's trun start, if it's an ai call the ai function.
    # if it's a player, wait for the player to click on the column to insert the piece
    # check for win after each turn
    # each turn the ai plays it should also open a gui window to draw minimax tree
    # if win, display the winner
    
    main_menu = MainMenu()
    main_menu.visualize()
    


if __name__ == "__main__":
    main()