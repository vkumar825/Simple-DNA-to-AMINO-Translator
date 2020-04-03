from main import *


def begin_conversion(import_file):
    try:
        imp = ImportSequence(import_file)  # To import the sequence, removing any new lines and make it into a string.
        sequence_str = imp.import_fasta()
        ver = ImportSequence(sequence_str)  # To verify if the sequence is valid, and make the sequence into a list of each letters.
        ver = ver.verify_fasta()
        rep = Sequence(ver)  # To replicate the DNA Sequence
        rep = rep.dna_replication()
        choice1 = input("Do you want to display DNA Replication? (Y/N): ")
        if choice1.upper() == 'Y':
            print('Sequence Length:', len(ver))
            print('Original DNA | Replicated DNA')
            replication_result = "\n".join(
                "\t {} \t\t - \t\t{}".format(x, y) for x, y in zip(ver, rep))
            print(replication_result)
        else:
            pass

        mrna = Sequence(rep)  # To transcribe into mRNA Sequence
        mrna = mrna.mRNA_transcription()
        choice2 = input("\nDo you want to display DNA Replication? (Y/N): ")
        if choice2.upper() == 'Y':
            print('\tDNA \t | \t  mRNA')
            transcribe_result = "\n".join(
                "\t {} \t\t - \t\t{}".format(x, y) for x, y in zip(ver, mrna))
            print(transcribe_result)
        else:
            pass
        print('Choose any key to represent a STOP and START protein codon.')
        print('You can choose to leave it blank if you want to see the whole thing.')
        start_input = input("Start character key: ")
        stop_input = input("Stop character key: ")
        protein = AminoAcids(mrna, start_input, stop_input)  # To convert to protein amino acids
        result = protein.amino_conversion()
        print("\nAmino Acids:", result)

    except FileNotFoundError:
        print("The '{}' file does not exist. Please make sure you have the correct file in a correct location".format(import_file))
