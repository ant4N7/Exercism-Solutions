def recite(start_verse, end_verse):

    verse = ['',                                                        #verse 1
             'malt that lay in the ',                                   #verse 2
             'rat that ate the ',                                       #verse 3
             'cat that killed the ',                                    #verse 4
             'dog that worried the ',                                   #verse 5
             'cow with the crumpled horn that tossed the ',             #verse 6
             'maiden all forlorn that milked the ',                     #verse 7
             'man all tattered and torn that kissed the ',              #verse 8
             'priest all shaven and shorn that married the ',           #verse 9
             'rooster that crowed in the morn that woke the ',          #verse 10
             'farmer sowing his corn that kept the ',                   #verse 11
             'horse and the hound and the horn that belonged to the ',  #verse 12
             'scalable python code that programmed the',                #starts adding verses
             'no matter how many verses, it couldn\'t be slowed, the'   #drops mic             
            ]
    
    insert = ''
    result = []
    
    for i in range(end_verse):
        insert = verse[i] + insert
        if i+1 >= start_verse:
            result.append(f'This is the {insert}house that Jack built.')

    return result
    