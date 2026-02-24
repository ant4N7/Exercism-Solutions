def to_rna(dna_strand):
    key = str.maketrans('GCTA ','CGAU ')
    return dna_strand.translate(key)