def DNA_strand(dna):
    '''
    A,T互补
    C,G互补
    :param dna: 输入DNA序列
    :return: 互补序列
    '''
    dnaList = list(dna)
    strand_dna = []
    for i in dnaList:
        if i == 'A': strand_dna.append('T')
        if i == 'T': strand_dna.append('A')
        if i == 'C': strand_dna.append('G')
        if i == 'G': strand_dna.append('C')
    return ''.join(strand_dna)

print(DNA_strand('ATTGC'))
print(DNA_strand('AAAA'))