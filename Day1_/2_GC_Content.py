from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
for record in SeqIO.parse(r"sequence.fasta", "fasta"):
    gc = gc_fraction(record.seq) * 100
    print(f"{record.id} |{len(record.seq)} bp |{gc:2f}% GC")
  
