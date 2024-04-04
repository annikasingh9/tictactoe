board = [[' ' for _ in range(3)] for _ in range(3)]


def create_board():
  for row in board:
    print(' | '.join(row))
  print()


def is_winner(player):
  for row in board:
    if row == [player, player, player]:
      return True
  
  
  for column in range(3):
    if board[0][column] == player and board[1][column] == player and board[2][column] == player:
      return True
  
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True


while True:
  create_board()
  while True:
    try:
      row = int(input('Player 1, enter the row(0,1,2): '))
      column = int(input('Player 1, enter the column(0,1,2): '))
      if board[row][column] == ' ':
        board[row][column] = 'X'
        break
    except (ValueError, IndexError):
      pass
    print('Invalid move, try again.')
  if is_winner('X'):
    print('Player 1 wins!')
    break

  
  create_board()
  while True:
    try:
      row = int(input('Player 2, enter the row(0,1,2): '))
      column = int(input('Player 2, enter the column(0,1,2): '))
      if board[row][column] == ' ':
        board[row][column] = 'O'
        break
    except (ValueError, IndexError):
      pass
    print('Invalid move, try again.')
  if is_winner('O'):
    print('Player 2 wins!')
    break
