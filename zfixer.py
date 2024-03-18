# Open and read the contents of tofix.txt
with open('tofix.txt', 'r') as file:
    lines = file.readlines()

# Initialize an empty string to hold the concatenated nucleotides
dna_sequence = ''

# Process each line to extract the nucleotide sequences
for line in lines:
    # Split the line into parts and ignore the first part (line number)
    parts = line.split()
    if len(parts) > 1:  # Check if the line contains nucleotides
        # Concatenate the nucleotide parts (excluding the first element which is the line number)
        dna_sequence += ''.join(parts[1:])

# Write the uninterrupted string of nucleotides to a .fasta file
with open('z.fasta', 'w') as output_file:
    # Write a header line
    output_file.write('>DNA_sequence\n')
    output_file.write(dna_sequence)
