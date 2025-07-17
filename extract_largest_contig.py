#!/usr/bin/env python3
"""
extract_largest_contig.py

This script extracts the largest contig from a FASTA file and writes it to a new file (largest_contig.fasta).
"""
import sys

def read_fasta(fasta_path):
    contigs = []
    header = None
    seq = []
    with open(fasta_path) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    contigs.append((header, ''.join(seq)))
                header = line
                seq = []
            else:
                seq.append(line)
        if header:
            contigs.append((header, ''.join(seq)))
    return contigs

def main():
    if len(sys.argv) != 2:
        print('Usage: python extract_largest_contig.py <input.fasta>')
        sys.exit(1)
    fasta = sys.argv[1]
    contigs = read_fasta(fasta)
    if not contigs:
        print('No contigs found!')
        sys.exit(1)
    largest = max(contigs, key=lambda x: len(x[1]))
    with open('largest_contig.fasta', 'w') as out:
        out.write(largest[0] + '\n')
        for i in range(0, len(largest[1]), 80):
            out.write(largest[1][i:i+80] + '\n')
    print('Largest contig written to largest_contig.fasta')
    print('Header:', largest[0])
    print('Length:', len(largest[1]))

if __name__ == '__main__':
    main()
