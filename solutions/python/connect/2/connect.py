"""x is left to right, o is top to bottom"""

class ConnectGame:
    def __init__(self, board: str) -> None:

        # convert the string into a list of strings
        board = board.splitlines()
        # format the strings to ensure correct spacing
        lines = [' '*i + line.strip() for i,line in enumerate(board)]

        # identify all possible starting and ending coordinates for X based on board size
        # create a set of coordinates representing all X's on the board
        # pack the three sets into variable x
        x_start = {(i,i) for i in range(len(lines))}
        x_end = {(i,len(r)-1) for i,r in enumerate(lines)}
        x_coord = {(r,c) for r,line in enumerate(lines) for c,char in enumerate(line) if char == 'X'}
        x = [x_start,x_end,x_coord]

        # repeate the above process for O's
        o_start = {(0,i) for i in range(0,len(lines[0]),2)}
        o_end = {(len(lines)-1,i) for i in range(len(board)-1,len(lines[-1]),2)}
        o_coord = {(r,c) for r,line in enumerate(lines) for c,char in enumerate(line) if char == 'O'}
        o = [o_start,o_end,o_coord]

        # conditional checks for setting _winner attribute
        if self._trace_path(o): self._winner = 'O'
        elif self._trace_path(x): self._winner = 'X'
        else: self._winner = ''

    def _trace_path(self,letter: list[set[tuple[int,int]]]) -> bool:
        """follow a letters path to see if it makes it from start to end"""

        # unpack the input data, initialize the path state and win condition
        starts,ends,coords = letter
        path_starts, path_ends = starts & coords, ends & coords

        #early return for no letters in the start or end cells
        if not path_starts or not path_ends:
            return False

        # main logic
        path = path_starts
        while not any(step in path_ends for step in path):
            temp = set()
            for step in path:
                r,c = step
                temp |= {(r,c+2),(r,c-2),(r+1,c+1),(r+1,c-1),(r-1,c+1),(r-1,c-1)}
            if path == path | temp & coords: return False
            path |= temp & coords
        return True

    def get_winner(self):
        return self._winner
