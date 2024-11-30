import math
from utils.board import Board
class Minimax:
    
    @classmethod
    def minimax_no_pruning(self, board, depth, maximazing_player):
        return self.minimax(board,depth,maximazing_player,pruning=False)

    @classmethod
    def minimax_pruning(self, board, depth, maximazing_player):
        return self.minimax(board,depth,maximazing_player,pruning=True)

    @classmethod
    def minimax(self, board, depth, maximazing_player, alpha=-math.inf, beta=math.inf, pruning=True):
        valid_col = board.get_valid_cols()
        is_terminal = board.is_terminal_node()

        if depth == 0 or is_terminal:
            player1_score, player2_score = board.get_scores()
            return None, player1_score - player2_score

        #maxmize the score
        if maximazing_player:
            best_col, max_util = None, -math.inf

            for col in valid_col:
                child_board = board.copy() 
                child_board.add_piece(col)
                _, util = self.minimax(child_board,depth-1,False)
                
                if util > max_util:
                    best_col, max_util = col, util

                if pruning:
                    alpha = max(alpha, max_util)

                    if alpha >= beta:
                        break

            return best_col, max_util

        #minimize the score
        else:
            best_col, min_util = None, math.inf

            for col in valid_col:
                child_board = board.copy() 
                child_board.add_piece(col)
                _, util = self.minimax(child_board,depth-1,True)

                if util < min_util:
                    best_col, min_util = col, util

                if pruning:
                    beta = min(beta,min_util)

                    if alpha >= beta:
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
  print(Minimax.minimax_pruning(board,math.inf,True))

