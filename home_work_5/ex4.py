class Cell:
    def __init__(self, number):
        self.number = number
        self.value = " "
        self.is_empty = True
    
    def set_value(self, value):
        if self.is_empty:
            self.value = value
            self.is_empty = False
            return True
        return False
    
    def __str__(self):
        return self.value if not self.is_empty else str(self.number)

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]
    
    def display(self):
        print("\n   Текущее поле:")
        for i in range(0, 9, 3):
            print(f" {self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} ")
            if i < 6:
                print("---+---+---")
        print()
    
    def make_move(self, cell_num, symbol):
        if 1 <= cell_num <= 9 and self.cells[cell_num-1].is_empty:
            return self.cells[cell_num-1].set_value(symbol)
        return False
    
    def check_winner(self):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        
        for combo in wins:
            a, b, c = combo
            if (self.cells[a].value == self.cells[b].value == self.cells[c].value 
                and not self.cells[a].is_empty):
                return self.cells[a].value
        
        if all(not cell.is_empty for cell in self.cells):
            return "Ничья"
        
        return None

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def make_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), ваш ход (1-9): "))
                if board.make_move(move, self.symbol):
                    return
                print("Клетка занята или не существует!")
            except ValueError:
                print("Введите число от 1 до 9!")

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player("Игрок 1", "X"),
            Player("Игрок 2", "O")
        ]
        self.current = 0
    
    def play(self):
        print("Крестики-Нолики!")
        print("Номера клеток:")
        demo = Board()
        demo.display()
        
        while True:
            self.board.display()
            player = self.players[self.current]
            player.make_move(self.board)
            
            result = self.board.check_winner()
            if result:
                self.board.display()
                if result == "Ничья":
                    print("Ничья!")
                else:
                    winner = next(p for p in self.players if p.symbol == result)
                    print(f"Победил {winner.name}!")
                break
            
            self.current = (self.current + 1) % 2

if __name__ == "__main__":
    game = Game()
    game.play()
