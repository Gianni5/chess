import chess


class Piece:
    def __init__(self, color):
        self.name = ""
        self.color = color

    def is_valid_move(self):
        return False

    def is_white(self):
        pass

    def __str__(self):
        if self.color:
            return self.name
        else:
            return '\033[1;30m' + self.name + '\033[0m'


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "R"

    def is_valid_move(self):
        return False


class Knight(Piece):
    def __init__(self, color):
        super(Knight, self).__init__(color)
        self.name = "N"

    def is_valid_move(self, board, start, finish):
        if abs(start[0] - finish[0]) == 2 and abs(start[1] - finish[1]) == 1:
            return True
        if abs(start[0] - finish[0]) == 1 and abs(start[1] - finish[1]) == 2:
            return True
        print("wrong path")
        return False


class Bishop(Piece):
    def __init__(self, color):
        super(Bishop, self).__init__(color)
        self.name = "B"

    def is_valid_move(self):
        return False


class Queen(Piece):
    def __init__(self, color):
        super(Queen, self).__init__(color)
        self.name = "Q"

    def is_valid_move(self):
        return False


class King(Piece):
    def __init__(self, color):
        super(King, self).__init__(color)
        self.name = "K"

    def is_valid_move(self):
        return False

    def can_castle(self):
        pass


class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "GP"

    def is_valid_move(self, board, start, to):
        return False


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"
        self.first_move = True

    def is_valid_move(self, board, start, finish):
        if self.color:


