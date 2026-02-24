BEGINNING = "I know an old lady who swallowed a {}."
ANIMALS = [None,"fly","spider","bird","cat","dog","goat","cow","horse"]
SPIDER = [""," that wriggled and jiggled and tickled inside her"]
FILL_LINES = [None,None,
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",    
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    ]
LINES = "She swallowed the {} to catch the {}{}."
ENDING = "I don't know why she swallowed the fly. Perhaps she'll die."
ALT_END = "She's dead, of course!"

def recite(start,end) -> list[str]:
    verse1 = [BEGINNING.format(ANIMALS[1]),ENDING]
    verse2 = [BEGINNING.format(ANIMALS[2]),
    FILL_LINES[2],
    LINES.format(ANIMALS[2],ANIMALS[1],SPIDER[0]),
    ENDING]
    verse3 = [BEGINNING.format(ANIMALS[3]),
    FILL_LINES[3],
    LINES.format(ANIMALS[3],ANIMALS[2],SPIDER[1]),
    LINES.format(ANIMALS[2],ANIMALS[1],SPIDER[0]),
    ENDING]
    verse4 = [BEGINNING.format(ANIMALS[4]),
    FILL_LINES[4],
    LINES.format(ANIMALS[4],ANIMALS[3],SPIDER[0]),
    LINES.format(ANIMALS[3],ANIMALS[2],SPIDER[1]),
    LINES.format(ANIMALS[2],ANIMALS[1],SPIDER[0]),
    ENDING]
    verse5 = [BEGINNING.format(ANIMALS[5]),
    FILL_LINES[5],
    LINES.format(ANIMALS[5],ANIMALS[4],SPIDER[0]),
    LINES.format(ANIMALS[4],ANIMALS[3],SPIDER[0]),
    LINES.format(ANIMALS[3],ANIMALS[2],SPIDER[1]),
    LINES.format(ANIMALS[2],ANIMALS[1],SPIDER[0]),
    ENDING]
    verse6 = [BEGINNING.format(ANIMALS[6]),
    FILL_LINES[6],
    LINES.format(ANIMALS[6],ANIMALS[5],SPIDER[0]),
    LINES.format(ANIMALS[5],ANIMALS[4],SPIDER[0]),
    LINES.format(ANIMALS[4],ANIMALS[3],SPIDER[0]),
    LINES.format(ANIMALS[3],ANIMALS[2],SPIDER[1]),
    LINES.format(ANIMALS[2],ANIMALS[1],SPIDER[0]),
    ENDING]
    verse7 = [BEGINNING.format(ANIMALS[7]),
    FILL_LINES[7],
    LINES.format(ANIMALS[7],ANIMALS[6],SPIDER[0]),
    LINES.format(ANIMALS[6],ANIMALS[5],SPIDER[0]),
    LINES.format(ANIMALS[5],ANIMALS[4],SPIDER[0]),
    LINES.format(ANIMALS[4],ANIMALS[3],SPIDER[0]),
    LINES.format(ANIMALS[3],ANIMALS[2],SPIDER[1]),
    LINES.format(ANIMALS[2],ANIMALS[1],SPIDER[0]),
    ENDING]
    verse8 = [BEGINNING.format(ANIMALS[8]),ALT_END]
    song = [None,verse1,verse2,verse3,verse4,verse5,verse6,verse7,verse8]
    result = []
    for verse in song[start:end+1]:
        result += verse + ['']
    return result[:-1]