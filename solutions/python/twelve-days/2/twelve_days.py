GIFTS = ['and a Partridge in a Pear Tree.','two Turtle Doves','three French Hens','four Calling Birds',
         'five Gold Rings','six Geese-a-Laying','seven Swans-a-Swimming','eight Maids-a-Milking',
         'nine Ladies Dancing','ten Lords-a-Leaping','eleven Pipers Piping','twelve Drummers Drumming']
DAYS = [None,'second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']


def recite(start_verse: int, end_verse: int) -> list[str]:
    verses = []
    if start_verse == 1:
        verses = ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.']
        for i in range(start_verse,end_verse):
            verses.append(f'On the {DAYS[i]} day of Christmas my true love gave to me: {", ".join(GIFTS[i::-1])}')
    else:
        for i in range(start_verse-1,end_verse):
            verses.append(f'On the {DAYS[i]} day of Christmas my true love gave to me: {", ".join(GIFTS[i::-1])}')
    return verses
