import math
from gui.tree import MinimaxNode
class Minimax:
    
    @classmethod
    def minimax_no_pruning(self, board, depth, maximazing_player):
        root = MinimaxNode(0,0)
        best_col, util = self.minimax(board,depth,maximazing_player,pruning=False,parent_node=root,layer=0)
        return best_col, util, root

    @classmethod
    def minimax_pruning(self, board, depth, maximazing_player):
        root = MinimaxNode(0,0)
        best_col, util= self.minimax(board,depth,maximazing_player,pruning=True,parent_node=root,layer=0)
        return best_col, util, root

    @classmethod
    def minimax(self, board, depth, maximizing_player, alpha=-math.inf, beta=math.inf, pruning=True, parent_node=None, layer=0):
        valid_col = board.get_valid_cols()
        is_terminal = board.is_terminal_node()

        if depth == 0 or is_terminal:
            player1_score, player2_score = board.get_heuristic_scores()
            parent_node.score = player1_score - player2_score
            return None, parent_node.score
        
        #maxmize the score
        if maximizing_player:
            best_col, max_util = None, -math.inf

            for col in valid_col:
                child_board = board.copy() 
                child_board.add_piece(col)
                child_node = MinimaxNode(0,layer+1)
                parent_node.add_child(child_node)

                _, util = self.minimax(board=child_board,
                                       depth=depth-1,
                                       maximizing_player=False,
                                       pruning=pruning,
                                       parent_node=child_node,
                                       layer=layer+1)
                
                if util > max_util:
                    best_col, max_util = col, util
                
                parent_node.score = max_util
                parent_node.best_move = best_col

                if pruning:
                    print("bonk")
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
                child_node = MinimaxNode(0,layer+1)
                parent_node.add_child(child_node)
                
                _, util = self.minimax(board=child_board,
                                       depth=depth-1,
                                       maximizing_player=True,
                                       pruning=pruning,
                                       parent_node=child_node,
                                       layer=layer+1)

                if util < min_util:
                    best_col, min_util = col, util

                parent_node.score = min_util
                parent_node.best_move = best_col

                if pruning:
                    print("bonk")
                    beta = min(beta,min_util)

                    if alpha >= beta:
                        break

            return best_col, min_util
           
            


