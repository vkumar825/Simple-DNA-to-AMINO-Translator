# simple-dna-sequencer

This is a simple DNA Sequencer built using Python. In this program, you can choose to import an existing DNA Sequence file, or generate one. After that, you have three options to choose which are...

- Replicate DNA Sequence (This replicates the DNA Sequence from the file, and corresponds the existing bases to the correct one, for ex. A-T, C-G and vice versa)
- Transcribe DNA To mRNA (This process is the same as the one above with the exception of T (which stands for Thymine) is replaced by U (Uracil)
-Translate DNA To Protein (This converts DNA to mRNA, which in turn is connected to python dictionary called codon_dict which has all the corresponding Amino Acids to the specific sequence of mRNA. During this process, you can choose to have which character represent a Start protein (Met) and STOP Protein.)
