import board


class Chess:

    def __init__(self):

        self.game = board.ChessBoard()
        self.turn = True

    def move(self, start, to):

        if self.game.board[start[0]][start[1]] is None:
            print("There is no piece to move at the start place")
            return

        target_piece = self.game.board[start[0]][start[1]]
        if self.turn != target_piece.color:
            print("That's not your piece to move")
            return

        end_piece = self.game.board[to[0]][to[1]]
        is_end_piece = end_piece is not None

        # Checks if a player's own piece is at the `to` coordinate
        if is_end_piece and self.game.board[start[0]][start[1]].color == end_piece.color:
            print("There's a piece in the path.")
            return

        if target_piece.is_valid_move(self.game, start, to):

            if self.game.board[to[0]][to[1]]:
                print(str(self.game.board[to[0]][to[1]]) + " taken.")

            self.game.board[to[0]][to[1]] = target_piece
            self.game.board[start[0]][start[1]] = None
            print(str(target_piece) + " moved.")  # needed

            self.turn = not self.turn


