# Game status categories_
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = '_'*len(word)
        self.correct_guesses = [None for _ in range(len(word))]

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError('The game has already ended.')
        if char not in self.word or char in self.correct_guesses:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
                return
        for i,ch in enumerate(self.word):
            if char == ch:
                self.correct_guesses[i] = char
        self.masked_word = ''.join('_' if ch is None else ch for ch in self.correct_guesses)
        if '_' not in self.masked_word:
            self.status = STATUS_WIN

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
