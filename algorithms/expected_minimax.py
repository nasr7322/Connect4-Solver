import math
from gui.tree import MinimaxNode
from utils.board import Board
from utils.enums import NodeType
class ExpectedMinimax:

      def __init__(self, board: Board, depth):
          self.board = board
          self.depth = depth
          self.root = MinimaxNode(0,0)
      
      def expected_minimax(self, node_type: NodeType, layer=0, depth=0, last_col=None):
          valid_cols = self.board.get_valid_cols()
          is_terminal = self.board.is_terminal_node()
          if self.depth == 0 or is_terminal:
              if node_type == NodeType.CHANCE_MIN or node_type == NodeType.CHANCE_MAX:
                  self.depth += 1
              else:
                player1_score, player2_score = self.board.get_heuristic_scores()
                return None, player1_score - player2_score
            
          if node_type == NodeType.MAX:
              best_col, max_util = None, -math.inf
              for col in valid_cols:
                  child_board = self.board.copy() 
                  # child_board.add_piece(col)
                  child_node = MinimaxNode(0,layer+1)
                  self.root.add_child(child_node)
                  _, util = self.expected_minimax(node_type=NodeType.CHANCE_MAX, layer=layer+1, depth=depth-1)
                  if util > max_util:
                      best_col, max_util = col, util
                  self.root.score = max_util
                  self.root.best_move = best_col
              return best_col, max_util
          elif node_type == NodeType.MIN:
              best_col, min_util = None, math.inf
              for col in valid_cols:
                  child_board = self.board.copy() 
                  # child_board.add_piece(col)
                  child_node = MinimaxNode(0,layer+1)
                  self.root.add_child(child_node)
                  _, util = self.expected_minimax(node_type=NodeType.CHANCE_MIN, layer=layer+1, depth=depth-1)
                  if util < min_util:
                      best_col, min_util = col, util
                  self.root.score = min_util
                  self.root.best_move = best_col
              return best_col, min_util
          else:
              valid_cols = [col for col in valid_cols if abs(col - last_col) <= 1]
              valid_cols_scores = []
              for col in valid_cols:
                  child_board = self.board.copy() 
                  child_board.add_piece(col)
                  child_node = MinimaxNode(0,layer+1)
                  self.root.add_child(child_node)
                  _, util = self.expected_minimax(node_type=(NodeType.MIN if node_type == NodeType.CHANCE_MAX else NodeType.MAX), layer=layer+1, depth=depth-1)
                  valid_cols_scores.append(util)
              util = 0
              for col, score in zip(valid_cols, valid_cols_scores):
                  if col == last_col:
                      weight = 0.6 + (0.4 if len(valid_cols) == 1 else 0)
                  else:
                      weight = 0.4 / (len(valid_cols) - 1)
                  util += weight * score
              return None, util

              
                  