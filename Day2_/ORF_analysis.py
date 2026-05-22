def find_orfs(sequence, min_length=150):
  orfs = []
  seq = str(sequence)
  stop_codons = ["TAA, "TAG", "TAG"]
  for i in range(len(seq) - 2):
  # Search for start codon
  if seq[i:i+3] == "ATG":
       # search for stop codon
       for j in range(i + 3, len(seq) - 2, 3):
           codon = seq[j:j+3]
           if codon in stop codons:
              orf_length = j - i + 3
              if orf_length >= min_length:
                  orfs.append((i, j + 3, orf_length))
              break
  return orfs
orfs = find_orfs(record.seq)
for start, stop, length in orfs:
    print(f"ORF: {start} -> {stop} |Length: {length} bp") 
