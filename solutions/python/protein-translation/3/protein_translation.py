CODON_CHART = {
    #UCAG
    'UUU UUC': 'Phenylalanine',
    'UUA UUG': 'Leucine',
    'UCU UCC UCA UCG': 'Serine',
    'UAU UAC': 'Tyrosine',
    'UAA UAG': 'STOP',
    'UGU UGC': 'Cysteine',
    'UGA': 'STOP',
    'UGG': 'Tryptophan',
    #CUU-CGG
    #AUU-AUA
    'AUG': 'Methionine'
    #ACU-AGG
    #GUU-GGG
}

def proteins(strand: str) -> list[str]:
    polypeptide = []
    for i in range(0,len(strand),3):
        codon = strand[i:i+3]
        if codon in 'UAA UAG UGA': #STOP
            return polypeptide
        for key in CODON_CHART.keys():
            if codon in key: polypeptide += [CODON_CHART[key]]
    return polypeptide
