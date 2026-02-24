class Scale:
    sharps = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    flats = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']
    flat_keys = ['F','Bb','Eb','Ab','Db','Gb','d','g','c','f','bb','eb']
    step_map = {'m':1,'M':2,'A':3}
    
    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        if self.tonic in self.flat_keys:
            i = self.flats.index(self.tonic.title())
            return self.flats[i:] + self.flats[:i]
        i = self.sharps.index(self.tonic.title())
        return self.sharps[i:] + self.sharps[:i]
        
    def interval(self, intervals):
        notes = self.chromatic()*2
        steps = list(intervals)[::-1]
        
        diatonic,i = [notes[0]],0
        while steps:
            i += self.step_map[steps.pop()]
            diatonic.append(notes[i])
        return diatonic
