import collections


class Garden:
    def __init__(self, matrix: list[str]):
        self._validate(matrix)
        self.height = len(matrix)
        self.width = len(matrix[0]) if matrix else 0
        self._annotate(matrix) # creates the following attributes:
        # self.flower_coordinates: set[tuple[int,int]]
        # self.empty_coordinates: set[tuple[int,int]]
        # self.annotations: CounterType[tuple[int,int]]
        # self.matrix: list[str]  <- complete with annotations
    
    def _validate(self, matrix):
        if len(set(len(row) for row in matrix)) > 1:
            raise ValueError('The board is invalid with current input.')
        for row in matrix:
            if not all(c in ' *' for c in row):
                raise ValueError('The board is invalid with current input.')
    
    def _annotate(self, matrix):
        self.flower_coordinates = set()
        self.empty_coordinates = set()
        for r, row in enumerate(matrix):
            for c, char in enumerate(list(row)):
                if char == '*':
                    self.flower_coordinates.add((r,c))
                elif char == ' ':
                    self.empty_coordinates.add((r,c))
        self.annotations = collections.Counter()
        for r,c in self.flower_coordinates:
            for dr,dc in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                nr,nc = r+dr, c+dc
                if (nr,nc) in self.empty_coordinates:
                    self.annotations[(nr,nc)] += 1
        self.matrix = [list(row) for row in matrix]
        for (r,c), v in self.annotations.items():
            self.matrix[r][c] = v
        self.matrix = [''.join(map(str,row)) for row in self.matrix]

def annotate(garden):
    return Garden(garden).matrix