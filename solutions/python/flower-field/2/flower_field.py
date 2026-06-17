import collections


def annotate(garden):
    class Garden:
        def __init__(self, matrix: list[str]):
            self.is_valid = len(set(len(row) for row in matrix)) <= 1
            if self.is_valid:
                self.height = len(matrix)
                self.width = len(matrix[0]) if matrix else 0
                self.flower_coordinates = set()
                self.empty_coordinates = set()
                for r, row in enumerate(matrix):
                    for c, char in enumerate(list(row)):
                        if char == '*':
                            self.flower_coordinates.add((r,c))
                        elif char == ' ':
                            self.empty_coordinates.add((r,c))
                        else:
                            self.is_valid = False
                            break
                    if not self.is_valid:
                        break
            if self.is_valid:
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
        
        def __str__(self):
            return '\n'.join(row for row in self.matrix)

    garden_object = Garden(garden)
    if garden_object.is_valid:
        return garden_object.matrix
    raise ValueError('The board is invalid with current input.')