from Bio import SeqIO
record = SeqIO.read("sequence.fasta", "fasta")
print("ID:", record.id)
print("Length:", len(record.seq))
print("first 25 bases:", record.seq[:25])
