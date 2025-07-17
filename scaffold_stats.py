#!/usr/bin/env python3
"""
scaffold_stats.py

Just a simple script to filter out short scaffolds (<2kb) from a FASTA file and print some stats.

"""
import sys
from pathlib import Path

def read_fasta(fasta_path):
    scaffolds = []
    header = None
    seq = []
    with open(fasta_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    scaffolds.append((header, ''.join(seq)))
                header = line
                seq = []
            else:
                seq.append(line)
        if header:
            scaffolds.append((header, ''.join(seq)))
    return scaffolds

def write_fasta(scaffolds, out_path):
    with open(out_path, 'w') as f:
        for h, s in scaffolds:
            f.write(h + '\n')
            for i in range(0, len(s), 80):
                f.write(s[i:i+80] + '\n')

def calc_stats(lengths):
    if not lengths:
        return 0, 0, 0, 0
    total = sum(lengths)
    longest = max(lengths)
    sorted_l = sorted(lengths, reverse=True)
    n50 = 0
    l50 = 0
    acc = 0
    for i, l in enumerate(sorted_l):
        acc += l
        if acc >= total / 2:
            n50 = l
            l50 = i + 1
            break
    return longest, total, n50, l50

def main():
    if len(sys.argv) != 3:
        print('Usage: python scaffold_stats.py <scaffolds.fasta> <filtered_output.fasta>')
        sys.exit(1)
    in_fasta = sys.argv[1]
    out_fasta = sys.argv[2]

    scaffolds = read_fasta(in_fasta)
    # Only keep scaffolds >= 2000 bp
    filtered = [(h, s) for h, s in scaffolds if len(s) >= 2000]
    lengths = [len(s) for h, s in filtered]
    longest, total, n50, l50 = calc_stats(lengths)
    write_fasta(filtered, out_fasta)
    print('Filtered scaffolds written to:', out_fasta)
    print('Number of scaffolds >=2kb:', len(filtered))
    print('Lengths:', lengths)
    print('Longest:', longest)
    print('Genome size:', total)
    print('N50:', n50)
    print('L50:', l50)
    print('Done!')

if __name__ == '__main__':
    main()


# This script can be run from the command line as follows:
# python3 scaffold_stats.py (input path) (output path)
# outputs for task 3 are in the pseudomonas folder in hybrid and illumina folders
# with the name scaffold_2kb.fasta 
#Output from my run was:
""" Filtered scaffolds written to: scaffolds.filtered.fasta
Number of scaffolds >=2kb: 6
Lengths: [9948, 9923, 5093, 5077, 5053, 4963]
Longest: 9948
Genome size: 40057
N50: 5093
L50: 3
Done! """