import random
import textwrap
import sys
from conversion_sequence import *


class ImportSequence:
    def __init__(self, file):
        self.file = file

    def import_fasta(self):
        sequence_letters = ''
        sequence_file = open(self.file, 'r')
        for each in sequence_file:
            sequence_letters = sequence_letters + each
            sequence_letters = sequence_letters.replace("\n", "")  # if the fasta is not in single-line already
            sequence_letters = sequence_letters.upper()  # if the fasta is not already upper-case

        return sequence_letters

    def verify_fasta(self):
        base_pair = ['A', 'C', 'T', 'G']
        sequence_list = []

        for i in range(len(self.file)):
            sequence_list.append(self.file[i])
            if sequence_list[i] in base_pair:
                pass
            else:
                print('The imported file does not have the correct information.')
                sys.exit()

        return sequence_list


class GenerateSequence:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def generate_file(self):
        N = 0
        generated_dna_sequence = ''
        while N != self.length:
            base_pair_key = ['a', 'c', 't', 'g']
            val = random.randint(0, 3)
            generated_dna_sequence += base_pair_key[val]
            N += 1

        file_write = open(self.name + '.txt', "w+")
        final_file = textwrap.fill(generated_dna_sequence, 70)
        file_write.write(final_file)
        file_write.close()

        return self.name + '.txt'


class Sequence:
    def __init__(self, sequence_list):
        self.sequence = sequence_list

    def dna_replication(self):
        dna_base_pairs = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
        replicated_dna_list = []

        for i in range(len(self.sequence)):
            if self.sequence[i] in dna_base_pairs:
                base_pair_val = dna_base_pairs[self.sequence[i]]
                replicated_dna_list.append(base_pair_val)

        return replicated_dna_list

    def mRNA_transcription(self):
        mRNA_base_pairs = {'A': 'U', 'G': 'C', 'T': 'A', 'C': 'G'}  # A (Adenine) pairs with U (Uracil)
        mRNA_transcript = ''

        for i in range(len(self.sequence)):
            if self.sequence[i] in mRNA_base_pairs:
                mRNA_pair_val = mRNA_base_pairs[self.sequence[i]]
                mRNA_transcript += mRNA_pair_val

        return mRNA_transcript

    def view_DNA(self):
        replicated_str = '- '
        for i in range(len(self.sequence)):
            replicated_str += self.sequence[i]

        return replicated_str

class AminoAcids:
    def __init__(self, mRNA_sequence, start_key, stop_key):
        self.mRNA = mRNA_sequence
        self.start = start_key
        self.stop = stop_key

    def amino_conversion(self):
        codon_dict = {
            'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
            'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
            'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'STOP', 'UAG': 'STOP',
            'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'STOP', 'UGG': 'Trp',
            'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
            'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
            'CAU': 'His', 'CAC': 'His', 'CAA': 'Gin', 'CAG': 'Gin',
            'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
            'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
            'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
            'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
            'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
            'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
            'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
            'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
            'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
        }

        mRNA_sequence = [self.mRNA[i:i + 3] for i in range(0, len(self.mRNA), 3)]  # splits the sequence by three characters
        protein = ''
        for i in range(len(mRNA_sequence)):
            if mRNA_sequence[i] in codon_dict:
                codon = codon_dict[mRNA_sequence[i]]
                protein += codon + ' '
            else:
                pass

        temp_sequence = protein.split()
        for i in range(len(temp_sequence)):
            if temp_sequence[i] == 'STOP':
                temp_sequence[i] = self.stop
            if temp_sequence[i] == 'Met':
                temp_sequence[i] = self.start

        final_protein = ''
        for i in range(len(temp_sequence)):
            final_protein += temp_sequence[i] + ' '

        return final_protein


def main():
    print('-------- DNA TO AMINO ACIDS ---------')
    print('      1) Import DNA Sequence')
    print('      2) Generate DNA Sequence')
    print('-------------------------------------')

    user_option = input('Option: ')

    if user_option == '1':
        import_file = input('Enter the name of the file to import: ')
        begin_conversion(import_file)

    if user_option == '2':
        sequence_file_name = input("Name of the file (without extension): ")
        sequence_length_input = int(input('Sequence Length: '))
        gen = GenerateSequence(sequence_file_name, sequence_length_input)
        gen = gen.generate_file()
        begin_conversion(gen)


if __name__ == '__main__':
    main()
