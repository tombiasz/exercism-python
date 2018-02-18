import re
import string


def to_rna(dna):
    if not re.match(r'^[GCTA]*$', dna):
        return ''

    trans_table = str.maketrans('GCTA', 'CGAU')
    return dna.translate(trans_table)
