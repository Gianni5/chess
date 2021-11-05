import pieces


class ChessBoard:
    def __init__(self):
        self.colon, row = (8, 8)
        self.board = [[None for i in range(row)] for j in range(self.colon)]

        # ------------------------black players
        self.board[0][0] = pieces.Rook(False)
        self.board[0][1] = pieces.Knight(False)
        self.board[0][2] = pieces.Bishop(False)
        self.board[0][3] = pieces.Queen(False)
        self.board[0][4] = pieces.King(False)
        self.board[0][5] = pieces.Bishop(False)
        self.board[0][6] = pieces.Knight(False)
        self.board[0][7] = pieces.Rook(False)

        self.board[1][0] = pieces.Pawn(False)
        self.board[1][1] = pieces.Pawn(False)
        self.board[1][2] = pieces.Pawn(False)
        self.board[1][3] = pieces.Pawn(False)
        self.board[1][4] = pieces.Pawn(False)
        self.board[1][5] = pieces.Pawn(False)
        self.board[1][6] = pieces.Pawn(False)
        self.board[1][7] = pieces.Pawn(False)
        # ------------------------white players
        self.board[6][0] = pieces.Pawn(True)
        self.board[6][1] = pieces.Pawn(True)
        self.board[6][2] = pieces.Pawn(True)
        self.board[6][3] = pieces.Pawn(True)
        self.board[6][4] = pieces.Pawn(True)
        self.board[6][5] = pieces.Pawn(True)
        self.board[6][6] = pieces.Pawn(True)
        self.board[6][7] = pieces.Pawn(True)

        self.board[7][0] = pieces.Rook(True)
        self.board[7][1] = pieces.Knight(True)
        self.board[7][2] = pieces.Bishop(True)
        self.board[7][3] = pieces.Queen(True)
        self.board[7][4] = pieces.King(True)
        self.board[7][5] = pieces.Bishop(True)
        self.board[7][6] = pieces.Knight(True)
        self.board[7][7] = pieces.Rook(True)

    def printing(self):

        print("    a   b   c   d   e   f   g   h")
        colon = 8
        for i in range(len(self.board)):
            colon -= 1
            tmp_str = "|"
            for j in self.board[i]:
                if j is None:
                    tmp_str += "   |"
                elif j.name == "GP":
                    return None
                else:
                    tmp_str += (" " + str(j) + " |")
            if self.board[i] is None:
                print("|   |")
            print(colon + 1, str(tmp_str), colon + 1)
        print("    a   b   c   d   e   f   g   h")
# x = ChessBoard()



