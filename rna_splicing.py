from Bio import SeqIO
from Bio.Seq import Seq

# Step 1: Read from input.txt in FASTA format
records = list(SeqIO.parse("input.txt","fasta"))

# First record is the full DNA sequence
main_dna = str(records[0].seq)

# Rest are introns
introns = [str(record.seq) for record in records[1:]]

# Step 2: Remove each intron from the main DNA string
for intron in introns:
    main_dna = main_dna.replace(intron,"")

# Step 3: Transcribe DNA to RNA (T -> U)
rna_seq = Seq(main_dna).transcribe()

# Step 4:Translate RNA to protein
protein = rna_seq.translate()

# Step 5: Print the final protein string
print(protein)
