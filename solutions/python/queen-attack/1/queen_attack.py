class Queen:

    square = tuple(tuple(r for r in range(11+i,19+i)) for i in range(0,71,10))

    def __init__(self, row, column):
        self.validate(row,column)
        self.row = row
        self.column = column
        self.position = self.square[row][column]

    @staticmethod
    def validate(row,column):
        if row < 0: raise ValueError('row not positive')
        if row > 7: raise ValueError('row not on board')
        if column < 0: raise ValueError('column not positive')
        if column > 7: raise ValueError('column not on board')
    
    def can_attack(self, another_queen):
        if self.position != another_queen.position:
            return any([not abs(self.position - another_queen.position)%11,
                        not abs(self.position - another_queen.position)%9,
                        self.row == another_queen.row,
                        self.column == another_queen.column])
        raise ValueError('Invalid queen position: both queens in the same square')
