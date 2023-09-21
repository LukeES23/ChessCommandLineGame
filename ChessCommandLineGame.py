import chess
import chess.svg # For rendering the board as SVG (optional)

def main():
    board = chess.Board()

    while not board.is_game_over():
        print(board)
        move = input("Enter your move (e.g.,  'e2e4'): ")
        if chess.Move.from_uci(move) in board.legal_moves:
            board.push(chess.Move.from_uci(move))
        else:
            print("Invalid move. Try again.")

    print("Game over. Result: " + board.result())
if __name__ == "__main__":
    main()
