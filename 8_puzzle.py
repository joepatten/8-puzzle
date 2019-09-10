import numpy as np
import subprocess as sp
import curses
import random

class puzzle():
    def __init__(self, board=None):
        self.goal_board = np.array([[1,2,3],[4,5,6],[7,8,' ']])
        if board == None:
            #self.board = np.array([[1,2,' '],[4,5,3],[7,8,6]])
            self.board = self.goal_board.copy()
        else:
            self.board = board
        self.location = np.where(self.board == ' ')
        self.location = np.array([self.location[0],self.location[1]])
        self.size = 3
        self.d = {'up':[[-1,0]], 'down':[[1,0]], 'left':[[0,-1]], 'right':[[0,1]]}
        self.randomize_board()
    
    def swap(self, r0, c0, r1, c1):
        self.board[r0, c0], self.board[r1, c1] = self.board[r1, c1], self.board[r0, c0]
        
    def move(self, direction):
        new_location = self.location + np.array(self.d[direction]).T
        if self.check_move(new_location):
            self.swap(*self.location, *new_location)
            self.location = new_location
    
    def do_all_moves(self):
        for direction in self.d.keys():
            self.move(direction)
            
    def check_move(self, new_location):
        return np.all(new_location < np.array([[3,3]]).T) and np.all(new_location >= np.array([[0,0]]).T)
    
    def check_board(self):
        return np.all(self.board == self.goal_board)
    
    def board_string(self):
        border = '+---+---+---+\n'
        board = border
        for row in self.board:
            board += '| ' + ' | '.join(row) + ' |\n'
            board += border
        return board
    
    def randomize_board(self):
        for i in range(30):
            direction = random.choice(list(self.d.keys()))
            self.move(direction)
        
    
if __name__ == "__main__":
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    screen.keypad(True)
    screen.addstr("Welcome to the 8 puzzle game.\n")
    p = puzzle()
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
        