CODON_CHART = {
    'UUU UUC': 'Phenylalanine',
    'UUA UUG': 'Leucine',
    'UCU UCC UCA UCG': 'Serine',
    'UAU UAC': 'Tyrosine',
    'UAA UAG UGA': 'STOP',
    'UGU UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    
    'AUG': 'Methionine'
}

def proteins(strand):
    polypeptide = []
    for i in range(0,len(strand),3):
        codon = strand[i:i+3]
        for key in CODON_CHART.keys():
            if codon in key: 
                if CODON_CHART[key] == 'STOP':
                    return polypeptide
                polypeptide += [CODON_CHART[key]]
    return polypeptide
