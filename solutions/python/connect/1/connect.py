"""x is left to right, o is top to bottom"""

class ConnectGame:
    def __init__(self, board):
        
        board = board.splitlines()
        lines = [' '*i + line.strip() for i,line in enumerate(board)]
        
        x_start = {(i,i) for i in range(len(lines))}
        x_end = {(i,len(r)-1) for i,r in enumerate(lines)}
        x_coord = {(r,c) for r,line in enumerate(lines) for c,char in enumerate(line) if char == 'X'}
        x = [x_start,x_end,x_coord]
        
        o_start = {(0,i) for i in range(0,len(lines[0]),2)}
        o_end = {(len(lines)-1,i) for i in range(len(board)-1,len(lines[-1]),2)}
        o_coord = {(r,c) for r,line in enumerate(lines) for c,char in enumerate(line) if char == 'O'}
        o = [o_start,o_end,o_coord]
        
        self._board_size = len(lines)*((len(lines[0])+1)//2)
        
        if self._trace_path(o): self._winner = 'O'
        elif self._trace_path(x): self._winner = 'X'
        else: self._winner = ''

    def _trace_path(self,letter):
        starts,ends,coords = letter
        path_starts, path_ends = starts & coords, ends & coords
        
        if len(path_starts) == 0 or len(path_ends) == 0:
            return False
        
        path = path_starts
        break_condition = 0
        while not any(step in path_ends for step in path):
            break_condition += 1
            temp = set()
            for step in path:
                r,c = step
                temp |= {(r,c+2),(r,c-2),(r+1,c+1),(r+1,c-1),(r-1,c+1),(r-1,c-1)}
            path |= temp
            path &= coords
            if break_condition == self._board_size: return False
        return True

    def get_winner(self):
        return self._winner
