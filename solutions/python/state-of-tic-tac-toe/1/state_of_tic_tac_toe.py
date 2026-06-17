class Board:
    def __init__(self, board: list[str]):
        self._build_coordinate_sets(board) # creates attributes:
        # self.x_coords: set[tuple[int,int]]
        # self.o_coords: set[tuple[int,int]]
        # self.empty_coords: set[tuple[int,int]]
        self.invalid_board_x_went_twice = len(self.x_coords) > len(self.o_coords)+1
        self.invalid_board_o_started = len(self.o_coords) > len(self.x_coords)
        self._set_win_condition_flags() # creates attributes:
        # self.x_win_condition_met: bool
        # self.o_win_condition_met: bool
        self.invalid_board_players_kept_playing_after_a_win = self.x_win_condition_met and self.o_win_condition_met
        self.gamestate = self._set_gamestate()

    def _build_coordinate_sets(self, board):
        self.x_coords = set()
        self.o_coords = set()
        self.empty_coords = set()
        for r, row in enumerate(board):
            for c, char in enumerate(row):
                if char == 'X':
                    self.x_coords.add((r,c))
                elif char == 'O':
                    self.o_coords.add((r,c))
                else:
                    self.empty_coords.add((r,c))
    
    def _set_win_condition_flags(self):
        win_coordinates = [
            ((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), 
            ((2,0),(2,1),(2,2)), ((0,0),(1,0),(2,0)), 
            ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)), 
            ((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0))
        ]
        self.x_win_condition_met = any(all(coords in self.x_coords for coords in group) for group in win_coordinates)
        self.o_win_condition_met = any(all(coords in self.o_coords for coords in group) for group in win_coordinates)
    
    def _set_gamestate(self) -> str:
        gs = {
            'ongoing':self.empty_coords and not self.x_win_condition_met and not self.o_win_condition_met,
            'draw':not self.empty_coords and not self.x_win_condition_met and not self.o_win_condition_met,
            'win':self.x_win_condition_met ^ self.o_win_condition_met
        }
        return 'ongoing' if gs['ongoing'] else 'draw' if gs['draw'] else 'win' if gs['win'] else 'invalid'


def gamestate(board):
    board_object = Board(board)
    if board_object.invalid_board_x_went_twice:
        raise ValueError('Wrong turn order: X went twice')
    if board_object.invalid_board_o_started:
        raise ValueError('Wrong turn order: O started')
    if board_object.invalid_board_players_kept_playing_after_a_win:
        raise ValueError('Impossible board: game should have ended after the game was won')
    return board_object.gamestate