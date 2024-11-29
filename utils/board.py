from .enums import Turn, Mode
class Board:
  def __init__(self, width=7, height=6, turn=Turn.AI, mode=Mode.MINIMAX, k_levels=4):
    self.width = width
    self.height = height
    self.board = [[Turn.NONE for _ in range(width)] for _ in range(height)]
    self.turn = turn
    self.player_1_actual_score = 0
    self.player_1_heuristic_score = 0
    self.player_2_actual_score = 0
    self.player_2_heuristic_score = 0

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

          if current_player == 1 and is_four:
            self.player_1_actual_score += 1
          elif current_player == 2 and is_four:
            self.player_2_actual_score += 1

  def update_heuristic(self):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # horizontal, vertical, diagonal, anti-diagonal
    self.player_1_heuristic_score = 0
    self.player_2_heuristic_score = 0
    for row in range(self.height):
      for col in range(self.width):
        for dr, dc in directions:
          current_x, current_y = col, row
          # get the beginning of the direction
          while 0 <= current_x < self.width and 0 <= current_y < self.height:
            current_x -= dc
            current_y -= dr
          current_player = self.board[row][col]
          score = 1
          for _ in range(4):
            current_x += dc
            current_y += dr
            if 0 <= current_x < self.width and 0 <= current_y < self.height and self.board[current_y][current_x] == current_player:
              score *= 2
            else:
              break
          if current_player == 1:
            self.player_1_heuristic_score += score
          elif current_player == 2:
            self.player_2_heuristic_score += score
        
          print(row, col, dr, dc, self.player_1_heuristic_score, self.player_2_heuristic_score)

  
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
