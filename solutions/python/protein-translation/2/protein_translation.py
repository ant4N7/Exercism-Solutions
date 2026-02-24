CODON_CHART = {
    'UUU UUC': 'Phenylalanine',
    'UUA UUG': 'Leucine',
    'UCU UCC UCA UCG': 'Serine',
    'UAU UAC': 'Tyrosine',
    'UAA UAG': 'STOP',
    'UGU UGC': 'Cysteine',
    'UGA': 'STOP',
    'UGG': 'Tryptophan',
    
    'AUG': 'Methionine'
}

def proteins(strand):
    polypeptide = []
    for i in range(0,len(strand),3):
        codon = strand[i:i+3]
        if codon in 'UAA UAG UGA':
            return polypeptide
        for key in CODON_CHART.keys():
            if codon in key: polypeptide += [CODON_CHART[key]]
    return polypeptide
