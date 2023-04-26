# source : https://www.ebi.ac.uk/ena/browser/view/SRX8325129

from Bio import SeqIO

# Replace 'your_fastq_file.fastq' with the path to your FASTQ file
fastq_file = 'SRR11771955.fastq'

# Iterate through the records in the FASTQ file
for record in SeqIO.parse(fastq_file, 'fastq'):
    # Access the sequence ID, sequence, and quality scores
    seq_id = record.id
    sequence = record.seq
    quality_scores = record.letter_annotations['phred_quality']

    # Print the sequence ID, sequence, and quality scores
    print(f'Sequence ID: {seq_id}')
    print(f'Sequence: {sequence}')
    print(f'Quality scores: {quality_scores}')
    print('---')