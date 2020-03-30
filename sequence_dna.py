import sys
import random

def start_sequencer():
    print("1) Import DNA Sequence")
    print("2) Generate DNA Sequence")

    sequence_letters = ''
    base_pair = 'ACTG'
    while True:
        user_choice = input("Your choice: ")
        if user_choice == '1':
            try:
                file_input = input("Enter the name of the file: ")
                sequence_file = open(file_input, 'r')
                for each in sequence_file:
                    sequence_letters = sequence_letters + each
                    sequence_letters = sequence_letters.upper()
                    sequence_letters = sequence_letters.replace("\n", "")

                sequence_list = [char for char in sequence_letters]  # makes the letter an each individual element

                if sequence_list[0] in base_pair:
                    pass
                else:
                    print('Imported file has incorrect information. Please try again')
                    break

                print("Choose one of the three options")
                print('1) Replicate DNA Sequence')
                print('2) Transcribe DNA To mRNA')
                print('3) Translate DNA To Protein')
                option_choice = input("Your choice: ")
                if option_choice == '1':
                    replicated = dna_replication(sequence_list)
                    print('\n')
                    print('Sequence Length:', len(sequence_list))
                    print('Original DNA | Replicated DNA')
                    replication_result = "\n".join("\t {} \t\t - \t\t{}".format(x, y) for x, y in zip(sequence_list, replicated))
                    print(replication_result)
                    sys.exit()

                if option_choice == '2':
                    rna_str = ''
                    for i in sequence_list:
                        rna_str += i
                    mRNA_letters = rna_str.replace("T", "U")
                    mRNA_sequence_list = [char for char in mRNA_letters]
                    print('\tDNA \t | \t  mRNA')
                    transcribe_result = "\n".join("\t {} \t\t - \t\t{}".format(x, y) for x, y in zip(sequence_list, mRNA_sequence_list))
                    print(transcribe_result)
                    print('Convert To Protein (Y/N)')
                    continue_choice = input("Your choice: ").upper()

                    if continue_choice == 'Y':
                        print('Choose a character key to represent START and STOP codon: ')
                        start_input = input("Start character key: ")
                        stop_input = input("Stop character key: ")
                        print('Amino Acids:', dna_to_protein(mRNA_letters, stop_input, start_input))
                        sys.exit()
                    else:
                        sys.exit()

                if option_choice == '3':
                    rna_str = ''
                    for i in sequence_list:
                        rna_str += i
                    mRNA_letters = rna_str.replace("T", "U")

                    print('Choose a character key to represent START and STOP codon: ')
                    start_input = input("Start character key: ")
                    stop_input = input("Stop character key: ")
                    print('Amino Acids:', dna_to_protein(mRNA_letters, stop_input, start_input))
                    sys.exit()

            except FileNotFoundError:
                print("Cannot find the file, please try again.")
        if user_choice == '2':
            while True:
                sequence_length_input = int(input('Sequence Length: '))
                n = 0
                generated_dna_sequence = ''
                while n != sequence_length_input:
                    base_pair_key = ['A', 'C', 'T', 'G']
                    val = random.randint(0, 3)
                    generated_dna_sequence += base_pair_key[val]
                    n += 1

                file_write = open('dna_sequence', "w+")
                file_write.write(generated_dna_sequence)
                file_write.close()

                sequence_file = open('dna_sequence', 'r')
                for each in sequence_file:
                    sequence_letters = sequence_letters + each
                    sequence_letters = sequence_letters.upper()
                    sequence_letters = sequence_letters.replace("\n", "")

                sequence_list = [char for char in sequence_letters]  # makes the letter an each individual element

                print("Choose one of the three options")
                print('1) Replicate DNA Sequence')
                print('2) Transcribe DNA To mRNA')
                print('3) Translate DNA To Protein')
                option_choice = input("Your choice: ")
                if option_choice == '1':
                    replicated = dna_replication(sequence_list)
                    print('\n')
                    print('Sequence Length:', len(sequence_list))
                    print('Original DNA | Replicated DNA')
                    replication_result = "\n".join(
                        "\t {} \t\t - \t\t{}".format(x, y) for x, y in zip(sequence_list, replicated))
                    print(replication_result)
                    sys.exit()

                if option_choice == '2':
                    rna_str = ''
                    for i in sequence_list:
                        rna_str += i
                    mRNA_letters = rna_str.replace("T", "U")
                    mRNA_sequence_list = [char for char in mRNA_letters]
                    print('\tDNA \t | \t  mRNA')
                    transcribe_result = "\n".join(
                        "\t {} \t\t - \t\t{}".format(x, y) for x, y in zip(sequence_list, mRNA_sequence_list))
                    print(transcribe_result)
                    print('Convert To Protein (Y/N)')
                    continue_choice = input("Your choice: ").upper()

                    if continue_choice == 'Y':
                        print('Choose a character key to represent START and STOP codon: ')
                        start_input = input("Start character key: ")
                        stop_input = input("Stop character key: ")
                        print('Amino Acids:', dna_to_protein(mRNA_letters, stop_input, start_input))
                        sys.exit()
                    else:
                        sys.exit()

                if option_choice == '3':
                    rna_str = ''
                    for i in sequence_list:
                        rna_str += i
                    mRNA_letters = rna_str.replace("T", "U")

                    print('Choose a character key to represent START and STOP codon: ')
                    start_input = input("Start character key: ")
                    stop_input = input("Stop character key: ")
                    print('Amino Acids:', dna_to_protein(mRNA_letters, stop_input, start_input))
                    sys.exit()



def dna_replication(dna_list):
    dna_base_pairs = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    replicated_dna_list = []

    for i in range(len(dna_list)):
        if dna_list[i] in dna_base_pairs:
            base_pair_val = dna_base_pairs[dna_list[i]]
            replicated_dna_list.append(base_pair_val)

    return replicated_dna_list


def dna_to_protein(mRNA, stop_key, start_key):
    codon_dict = {
        'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'STOP', 'UAG': 'STOP',
        'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'STOP', 'UGG': 'Trp',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'CAU': 'His', 'CAC': 'His', 'CAA': 'Gin', 'CAG': 'Gin',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',  # Met is the Start Protein
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
        'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
    }

    mRNA_sequence = [mRNA[i:i + 3] for i in range(0, len(mRNA), 3)]  # splits the mRNA sequence into every three characters
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
            temp_sequence[i] = stop_key
        if temp_sequence[i] == 'Met':
            temp_sequence[i] = start_key

    final_protein = ''
    for i in range(len(temp_sequence)):
        final_protein += temp_sequence[i] + ' '

    return final_protein


if __name__ == '__main__':
    start_sequencer()
