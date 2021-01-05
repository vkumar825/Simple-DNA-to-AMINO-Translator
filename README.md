# DNA-to-AMINO-Translator

This is a simple DNA to Amino Translator built using Python. In this program, you can choose to import an existing file that contains a DNA Sequence file, or generate one. You are not limited by the amount you want to generate, whether you want to have the length of 10, or even higher up to the length of 1000 base pairs. But it is reccommended to keep the length of the sequence below 1000 as to not clutter the output terminal. 

After importing the file, or generating it, there are two more additional options which are...

- View DNA Replication (This replicates the DNA Sequence from the file, and corresponds the existing bases to the correct one, for ex. A-T, C-G and vice versa)

- View mRNA Translation (This process is the same as the one above with the exception of T (Thymine) is replaced by U (Uracil)

Finally, you can choose to have which character key represent a Start protein (Met) and STOP Protein as this program converts the mRNA Sequence (which in turn was translated from DNA Sequence) as to identify where those protein codon are. In order to the correctly identify amino protein codons, the program uses python dictionary called codon_dict which has all the corresponding Amino Acids to the specific sequence of mRNA.
