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

def is_spider(i):
    return ANIMALS[i] == "spider"

def generate_lines(start):
    return [LINES.format(ANIMALS[i],ANIMALS[i-1],SPIDER[is_spider(i-1)]) for i in range(start,1,-1)]

def generate_verse(i):
    return [BEGINNING.format(ANIMALS[i]),FILL_LINES[i]]+generate_lines(i)+[ENDING]

def generate_song():
    return [None,[BEGINNING.format(ANIMALS[1]),ENDING]]+ \
    [generate_verse(i) for i in range(2,8)]+ \
    [[BEGINNING.format(ANIMALS[8]),ALT_END]]

def recite(start,end) -> list[str]:
    song = generate_song()
    return [line for verse in song[start:end+1] for line in verse + ['']][:-1]