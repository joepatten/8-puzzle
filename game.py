import curses
from puzzle_board import Puzzle


def play_game():
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    screen.keypad(True)
    screen.addstr("Welcome to the 8 puzzle game.\n")
    p = Puzzle()
    screen.addstr("Press any button to begin the game.\n")
    screen.getch()

    moves = 0
    while True:
        screen.clear()
        screen.addstr('Use the arrow keys to move the blank square. Press Esc or e to exit.\n')
        screen.addstr(p.board_string())
        if p.check_board():
            screen.addstr(f'You won in {moves} moves. Hooray.\nPress any key to exit.')
            screen.getch()
            break
        c = screen.getch()
        if c == ord('e') or c == 27:
            break
        elif c == ord('w') or c == 259:
            p.move('up')
        elif c == ord('s') or c == 258:
            p.move('down') 
        elif c == ord('a') or c == 260:
            p.move('left')
        elif c == ord('d') or c == 261:
            p.move('right')
        else:
            continue
        moves += 1
        screen.refresh()


    curses.noecho()
    curses.cbreak()
    curses.curs_set(1)
    screen.keypad(False)
    curses.endwin()


if __name__ == "__main__":
    play_game()