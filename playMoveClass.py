from colorama import Back, Fore, init

if __name__ == "__main__":
    init()  # Initialize colorama

class CFB:
    def __init__(self):  # Correct method name for the constructor
        self.board = [['#' for _ in range(7)] for _ in range(6)]

    def play_move(self, row, column, letter):
        if letter == 'O':
            print(Back.CYAN)
            self.board[row][column] = letter
            print(Back.WHITE)
        self.board[row][column] = letter

    def get_value(self, row, column):
        PiC = self.board[row][column]
        return PiC

    def print_board(self):
        print(Fore.BLUE + Back.BLUE + " 1   2   3   4   5   6   7")  # Use Fore.BLUE and Back.BLUE to specify the foreground and background colors
        for row in self.board:
            row_str = ""
            for cell in row:
                row_str += " " + str(cell) + " |"
            print(Fore.WHITE + Back.WHITE + row_str)  # Use Fore.WHITE and Back.WHITE to specify the foreground and background colors
