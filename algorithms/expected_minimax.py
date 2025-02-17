import math
from gui.tree import MinimaxNode
from utils.board import Board
from utils.enums import NodeType
class ExpectedMinimax:

      def __init__(self, board: Board, depth):
          self.board = board
          self.depth = depth
          self.root = MinimaxNode(0,0)
          self.memory = {}
          self.node_expanded = 0
      
      def expected_minimax(self):
          best_col, util = self.expected_minimax_util(node_type=NodeType.MIN, layer=0, depth=self.depth, last_col=None, board=self.board, parent_node=self.root)
          return best_col, util, self.root

      def expected_minimax_util(self, node_type: NodeType, layer=0, depth=0, last_col=None, board=None, parent_node=None):
          if (board.get_hash(), node_type, last_col) in self.memory:
              return self.memory[(board.get_hash(), node_type, last_col)]
          
          valid_cols = board.get_valid_cols()
          is_terminal = board.is_terminal_node()

          self.node_expanded += 1

          if depth == 0 or is_terminal:
              if depth == 0 and (node_type == NodeType.CHANCE_MIN or node_type == NodeType.CHANCE_MAX):
                  depth += 1
              else:
                player1_score, player2_score = board.get_heuristic_scores()
                parent_node.score = player1_score - player2_score
                return None, player1_score - player2_score
          

          if node_type == NodeType.MAX:
              best_col, max_util = None, -math.inf
              for col in valid_cols:
                  child_board = board.copy() 
                  child_node = MinimaxNode(0, layer + 1)
                  parent_node.add_child(child_node)
                  _, util = self.expected_minimax_util(node_type=NodeType.CHANCE_MAX, layer=layer+1, depth=depth-1, last_col=col, board=child_board, parent_node=child_node)
                  if util > max_util:
                      best_col, max_util = col, util
                  parent_node.score = max_util
                  parent_node.best_move = best_col
              self.memory[(board.get_hash(), node_type, last_col)] = (best_col, max_util)
              return best_col, max_util
          elif node_type == NodeType.MIN:
              best_col, min_util = None, math.inf
              for col in valid_cols:
                  child_board = board.copy() 
                  child_node = MinimaxNode(0, layer + 1)
                  parent_node.add_child(child_node)
                  _, util = self.expected_minimax_util(node_type=NodeType.CHANCE_MIN, layer=layer+1, depth=depth-1, last_col=col, board=child_board, parent_node=child_node)
                  if util < min_util:
                      best_col, min_util = col, util
                  parent_node.score = min_util
                  parent_node.best_move = best_col
              self.memory[(board.get_hash(), node_type, last_col)] = (best_col, min_util)
              return best_col, min_util
          else:
              valid_cols = [col for col in valid_cols if abs(col - last_col) <= 1]
              valid_cols_scores = []
              for col in valid_cols:
                  child_board = board.copy() 
                  child_board.add_piece(col)
                  child_node = MinimaxNode(0, layer + 1)
                  parent_node.add_child(child_node)
                  _, util = self.expected_minimax_util(node_type=(NodeType.MIN if node_type == NodeType.CHANCE_MAX else NodeType.MAX), layer=layer+1, depth=depth-1, board=child_board, parent_node=child_node)
                  valid_cols_scores.append(util)
              util = 0
              for col, score in zip(valid_cols, valid_cols_scores):
                  if col == last_col:
                      weight = 0.6 + (0.4 if len(valid_cols) == 1 else 0)
                  else:
                      weight = 0.4 / (len(valid_cols) - 1)
                  util += weight * score
              parent_node.score = util
              self.memory[(board.get_hash(), node_type, last_col)] = (None, util)
              return None, util

      