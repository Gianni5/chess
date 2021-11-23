blocked_path = "There's a piece in the path."
incorrect_path = "This piece does not move in this pattern."


class Piece:
    """
    A class to represent a piece in chess

    ...

    Attributes:
    -----------
    name : str
        Represents the name of a piece as following -
        Pawn -> P
        Rook -> R
        Knight -> N
        Bishop -> B
        Queen -> Q
        King -> K

    color : bool
        True if piece is white

    Methods:
    --------
    is_valid_move(board, start, to) -> bool
        Returns True if moving the piece at `start` to `to` is a legal
        move on board `board`
        Precondition: [start] and [to] are valid coordinates on the game.board
    is_white() -> bool
        Return True if piece is white

    """

    def __init__(self, color):
        self.name = ""
        self.color = color

    def is_valid_move(self, game, start, to):
        if self.color:
            # diagonal move
            if start[0] == to[0] + 1 and (start[1] == to[1] + 1 or start[1] == to[1] - 1):
                if game.board[to[0]][to[1]] is not None:
                    self.first_move = False
                    return True
                print("Cannot move diagonally unless taking.")
                return False

            # vertical move for white pieces
            if start[1] == to[1]:
                if (start[0] - to[0] == 2 and self.first_move) or (start[0] - to[0] == 1):
                    for i in range(start[0] - 1, to[0] - 1, -1):
                        if game.board[i][start[1]] is not None:
                            print(blocked_path)
                            return False
                    self.first_move = False
                    return True
                print("Invalid move" + " or " + "Cannot move forward twice if not first move.")
                return False
            print(incorrect_path)
            return False
        # vertical move for black pieces
        else:
            if start[0] == to[0] - 1 and (start[1] == to[1] - 1 or start[1] == to[1] + 1):
                if game.board[to[0]][to[1]] is not None:
                    self.first_move = False
                    return True
                print(blocked_path)
                return False
            if start[1] == to[1]:
                if (to[0] - start[0] == 2 and self.first_move) or (to[0] - start[0] == 1):
                    for i in range(start[0] + 1, to[0] + 1):
                        if game.board[i][start[1]] is not None:
                            print(blocked_path)
                            return False
                    self.first_move = False
                    return True
                print("Invalid move" + " or " + "Cannot move forward twice if not first move.")
                return False
            print(incorrect_path)
            return False

    def is_white(self):
        return self.color

    def __str__(self):
        if self.color:
            return self.name
        else:
            return '\033[1;30m' + self.name + '\033[0m'


class Rook(Piece):
    def __init__(self, color, first_move=True):
        """
        Same as base class Piece, except `first_move` is used to check
        if this rook can castle.
        """
        super().__init__(color)
        self.name = "R"
        self.first_move = first_move

    def is_valid_move(self, game, start, to):
        return super().is_valid_move(game, start, to)


class Knight(Piece):
    def __init__(self, color, first_move=True):
        super().__init__(color)
        self.name = "N"
        self.first_move = first_move

    def is_valid_move(self, game, start, to):
        return super().is_valid_move(game, start, to)


class Bishop(Piece):
    def __init__(self, color, first_move=True):
        super().__init__(color)
        self.name = "B"
        self.first_move = first_move

    def is_valid_move(self, game, start, to):
        return super().is_valid_move(game, start, to)


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"
        self.first_move = True

    def is_valid_move(self, game, start, to):
        return super().is_valid_move(game, start, to)


class King(Piece):
    def __init__(self, color, first_move=True):
        """
        Same as base class Piece, except `first_move` is used to check
        if this king can castle.
        """
        super().__init__(color)
        self.name = "K"
        self.first_move = first_move

    def is_valid_move(self, game, start, to):
        return super().is_valid_move(game, start, to)

    def castle(self, board, input, turn):
        if turn is False:

            # check if black king has  moved
            if board[0][4].name == "K" and self.first_move and self.color is False and input == "o-o":
                # check if rook has moved
                if board[0][7].name == "R" and self.first_move:
                    # check if any piece in between
                    if board[0][5] and board[0][6] is not None:
                        print("you can't castle")
                        return

                    else:
                        board[0][6] = King(False)
                        # delete king from original position
                        board[0][4] = None
                        board[0][5] = Rook(False)
                        board[0][7] = None
                        return print("King castled")

            # check if black king has  moved
            if board[0][4].name == "K" and self.first_move and self.color is False and input == "o-o-o":
                # check if rook has moved
                if board[0][0].name == "R" and self.first_move:
                    # check if any piece in between
                    if board[0][3] and board[0][2] and board[0][1] is not None:
                        print("you can't castle")
                        return

                    else:
                        board[0][1] = King(False)
                        # delete king from original position
                        board[0][4] = None
                        board[0][2] = Rook(False)
                        board[0][0] = None
                        return print("King castled")
        else:
            if board[7][4] is None:
                return print("castle not possible")
            # check if white king has  moved
            if board[7][4].name == "K" and self.first_move and input == "o-o":
                # check if rook has moved
                if board[7][7].name == "R" and self.first_move:
                    # check if any piece in between
                    if board[7][5] and board[7][6] is not None:
                        print("you can't castle")
                        return

                    else:
                        board[7][6] = King(True)
                        # delete king from original position
                        board[7][4] = None
                        board[7][5] = Rook(True)
                        board[7][7] = None
                        return print("King castled")

            if board[7][4] is None:
                return print("castle not possible")
            # check if king has  moved
            if board[7][4].name == "K" and self.first_move and input == "o-o-o":

                # check if rook has moved
                if board[7][0].name == "R" and self.first_move:
                    # check if any piece in between
                    if board[7][3] and board[7][2] and board[7][1] is not None:
                        print("you can't castle")
                        return

                    else:
                        board[7][1] = King(True)
                        # delete king from original position
                        board[7][4] = None
                        board[7][2] = Rook(True)
                        board[7][0] = None
                        return print("King castled")


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"
        self.first_move = True

    def is_valid_move(self, game, start, to):
        return super().is_valid_move(game, start, to)


'''x = [[(i, j) for j in range(8)] for i in range(8)]

for i in x:
    print(i)'''
'''list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(list1[1:3][:])
""" [1:3] is used for rows-1,2[:] is used to represent all values"""
list1[0].append(6)
print(list1)'''
