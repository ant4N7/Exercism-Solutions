class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        self.rows = [row.split(' ') for row in rows]
        self.columns = [col for col in zip(*self.rows)]

    def row(self, index):
        return [int(el) for el in self.rows[index-1]]

    def column(self, index):
        return [int(el) for el in self.columns[index-1]]
