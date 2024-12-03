import math
import time
from gui.tree import MinimaxNode
from utils.board import Board
class Minimax:
    def __init__(self, board: Board, depth, maximizing_player):
        self.board = board
        self.depth = depth
        self.maximizing_player = maximizing_player
        self.memory = {}
        self.node_expanded = 0

    def minimax_no_pruning(self):
        root = MinimaxNode(0, 0)
        best_col, util = self.minimax(self.depth, self.maximizing_player, pruning=False, parent_node=root, layer=0)
        return best_col, util, root

    def minimax_pruning(self):
        root = MinimaxNode(0, 0)
        best_col, util = self.minimax(self.depth, self.maximizing_player, pruning=True, parent_node=root, layer=0)
        return best_col, util, root

    def minimax(self, depth, maximizing_player, alpha=-math.inf, beta=math.inf, pruning=True, parent_node:MinimaxNode=None, layer=0):
        # print("Check", self.board.get_hash())
        if self.board.get_hash() in self.memory:
            # print("Memory hit")
            # print(self.board.get_hash())
            return self.memory[self.board.get_hash()]
        
        valid_cols = self.board.get_valid_cols()
        is_terminal = self.board.is_terminal_node()

        self.node_expanded += 1

        if depth == 0 or is_terminal:
            player1_score, player2_score = self.board.get_heuristic_scores()
            parent_node.score = player1_score - player2_score
            return None, parent_node.score

        if maximizing_player:
            best_col, max_util = None, -math.inf

            for col in valid_cols:
                self.board.add_piece(col)
                child_node = MinimaxNode(0, layer + 1)
                parent_node.add_child(child_node)

                _, util = self.minimax(depth - 1, False, alpha, beta, pruning, child_node, layer + 1)

                self.board.remove_piece(col)

                if util > max_util:
                    best_col, max_util = col, util

                parent_node.score = max_util
                parent_node.best_move = best_col

                if pruning:
                    alpha = max(alpha, max_util)
                    if alpha >= beta:
                        break
            # print("MAX", self.board.get_hash())
            self.memory[self.board.get_hash()] = (best_col, max_util)
            return self.memory[self.board.get_hash()]

        else:
            best_col, min_util = None, math.inf

            for col in valid_cols:
                self.board.add_piece(col)
                child_node = MinimaxNode(0, layer + 1)
                parent_node.add_child(child_node)

                _, util = self.minimax(depth - 1, True, alpha, beta, pruning, child_node, layer + 1)

                self.board.remove_piece(col)

                if util < min_util:
                    best_col, min_util = col, util

                parent_node.score = min_util
                parent_node.best_move = best_col

                if pruning:
                    beta = min(beta, min_util)
                    if alpha >= beta:
                        break
            # print("MIN", self.board.get_hash())
            self.memory[self.board.get_hash()] = (best_col, min_util)
            return self.memory[self.board.get_hash()]