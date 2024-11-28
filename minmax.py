import math
from board import Board
class Minmax:
    
    @classmethod
    def minmax(self, board, depth, maximazing_player, alpha=-math.inf, beta=math.inf, pruning=True):
        valid_col = board.get_valid_cols()
        is_terminal = board.is_terminal_node()

        if depth == 0 or is_terminal:
            player1_score, player2_score = board.get_scores()
            return None, player1_score - player2_score

        #maxmize the score
        if maximazing_player:
            best_col, max_util = None, -math.inf

            for col in valid_col:
                child_board = board.copy() # could be optimized by backtracking
                child_board.add_piece(col)
                _, util = self.minmax(child_board,depth-1,False)
                
                if util > max_util:
                    best_col, max_util = col, util

                alpha = max(alpha, max_util)

                if pruning and alpha >= beta:
                    break

            return best_col, max_util

        #minimize the score
        else:
            best_col, min_util = None, math.inf

            for col in valid_col:
                child_board = board.copy() # could be optimized by backtracking
                child_board.add_piece(col)
                _, util = self.minmax(child_board,depth-1,True)

                if util < min_util:
                    best_col, min_util = col, util

                beta = min(beta,min_util)

                if pruning and alpha >= beta:
                    break

            return best_col, min_util
           
            
if __name__ == "__main__":
  board = Board()
  board.add_piece(0)
  board.add_piece(0)
  board.add_piece(0)
  board.add_piece(1)
  board.add_piece(0)
  board.add_piece(1)
  board.add_piece(0)
  board.add_piece(1)
  board_view = board.get_board()
  for row in board_view:
    print(row)
  print(board.get_scores())
  print(Minmax.minmax(board,math.inf,False))

