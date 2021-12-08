import os
import sys

gff_in = sys.argv[1]

file_name_list = gff_in.split('.')
file_name_prefix = '_'.join(file_name_list[:-1])

gff_feature = ['gene', 'mRNA', 'CDS', 'exon']

with open(gff_in, 'r') as f:
    for line in f:
        line_list = line.split('\t')
        if len(line_list) != 9:
            continue
        elif line_list[2] in gff_feature:
            print('\t'.join(line_list).rstrip('\r\n'))
        