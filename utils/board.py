import copy
import random

from .enums import Turn, Mode

class Board:
  def __init__(self, width=7, height=6, turn=Turn.AI, mode=Mode.MINIMAX):
    self.width = width
    self.height = height
    self.board = [[Turn.NONE for _ in range(width)] for _ in range(height)]
    self.turn = turn
    self.player_1_actual_score = 0
    self.player_1_heuristic_score = 0
    self.player_2_actual_score = 0
    self.player_2_heuristic_score = 0
    self.mode = mode

  def get_board(self):
    return self.board
  
  def get_cell(self, row, col):
    return self.board[row][col]

  def get_scores(self):
    return self.player_1_actual_score, self.player_2_actual_score
  
  def get_heuristic_scores(self):
    return self.player_1_heuristic_score, self.player_2_heuristic_score
  
  def get_player_turn(self):
    return self.turn == Turn.AI
  
  def add_piece(self, col):
    valid_cols = [c for c in self.get_valid_cols() if abs(c - col) <= 1]
    if col not in valid_cols:
      return False
    
    if self.mode == Mode.EXPECTED_MINIMAX:
      thresh_target = 60 + (40 if len(valid_cols) == 1 else 0)
      thresh_left = (40 / (len(valid_cols)-1) + thresh_target) if (col-1) in valid_cols else thresh_target
      thresh_right = 40 / (len(valid_cols)-1) + thresh_left if (col+1) in valid_cols else thresh_left

      rand_sample = random.randint(0, 100)
      print(rand_sample, thresh_target, thresh_left, thresh_right)
      if thresh_target < rand_sample < thresh_left:
        col -= 1
      elif thresh_left < rand_sample < thresh_right:
        col += 1

    for row in range(self.height):
      if (row + 1 == self.height or self.board[row + 1][col] != Turn.NONE) and self.board[row][col] == Turn.NONE:
        self.board[row][col] = self.turn
        self.turn = Turn.HUMAN if self.turn == Turn.AI else Turn.AI
        self.update_scores()
        return True
    return False
  
  def update_scores(self):
    self.update_heuristic()
    self.update_actual_scores()
  
  def update_actual_scores(self):
    self.player_1_actual_score = 0
    self.player_2_actual_score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for row in range(self.height):
      for col in range(self.width):
        for dr, dc in directions:
          current_player = self.board[row][col]
          is_four = True
          for piece in range(4):
            current_x = col + dc * piece
            current_y = row + dr * piece
            if not (0 <= current_x < self.width and 0 <= current_y < self.height and self.board[current_y][current_x] == current_player):
              is_four = False
              break

          if current_player == Turn.AI and is_four:
            self.player_1_actual_score += 1
          elif current_player == Turn.HUMAN and is_four:
            self.player_2_actual_score += 1

  def update_heuristic(self):
    self.player_1_heuristic_score = 0
    self.player_2_heuristic_score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # right, down, diagonal right, diagonal left
    for row in range(self.height):
      for col in range(self.width):
        for dr, dc in directions:
          current_player = self.board[row][col]
          score = 1
          for piece in range(4):
            current_x = col + dc * piece
            current_y = row + dr * piece
            if not (0 <= current_x < self.width and 0 <= current_y < self.height and self.board[current_y][current_x] == current_player):
              break
            score *= 2
          score /= 2

          if current_player == Turn.AI:
            self.player_1_heuristic_score += score
          elif current_player == Turn.HUMAN:
            self.player_2_heuristic_score += score
          print(current_player, score, f"{dr},{dc}")
        print(row, col, self.player_1_heuristic_score, self.player_2_heuristic_score)


        

  def get_valid_cols(self):
    valid_cols = []
    for col in range(0,self.width):
      if self.board[0][col] == Turn.NONE:
        valid_cols.append(col)

    return valid_cols
  
  def is_terminal_node(self):
    for col in range(0,self.width):
      if self.board[0][col] == Turn.NONE:
        return False      
    return True
  
  def copy(self):
    return copy.deepcopy(self)
         
  
if __name__ == "__main__":
  board = Board()
  board.add_piece(0)
  board.add_piece(1)
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
