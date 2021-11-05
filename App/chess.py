import board
import pieces


class Chess:
    def __init__(self):
        self.board = board.ChessBoard()
        self.turn = True

        self.white_ghost_piece = None
        self.black_ghost_piece = None

    def move(self, start, finish):

        if self.board.board[start[0]][start[1]] is None:
            print("no piece to move")
            return
        target_piece = self.board.board[start[0]][start[1]]
        if self.turn != target_piece.color:
            print("this is not your piece")
            return

        blocked_path = self.board.board[finish[0]][finish[1]]
        is_path_blocked = blocked_path is not None

        if is_path_blocked and target_piece.color == blocked_path.color:
            print("there is piece on the path")
            return


def translate(s):
    """
    Translates traditional board coordinates of chess into list indices
    """
    try:
        row = int(s[0])
        col = s[1]
        if row < 1 or row > 8:
            print(s[0] + "is not in the range from 1 - 8")
            return None
        if col < 'a' or col > 'h':
            print(s[1] + "is not in the range from a - h")
            return None
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return 8 - row, dict[col]
    except:
        print(s + "is not in the format '[number][letter]'")
        return None


if __name__ == "__main__":
    chess = Chess()
    chess.board.printing()

    while True:
        start = input("From: ")
        finish = input("To: ")

        start = translate(start)
        finish = translate(finish)

        if start is None or finish is None:
            continue

        chess.move(start, finish)
        chess.board.printing()
