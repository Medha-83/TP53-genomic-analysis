record = SeqIO.read(r"sequence.fasta", "fasta")
seq = record.seq
window = 100
step = 10
gc_values = []
position = []
for i in range (0, len(seq)-window, step):
  chunk = seq[i:i + window]
  gc_values.append(gc_fraction(chunk)*100)
  position.append(i)
plt.plot(position, gc_values)
plt.xlabel("position(bp)")
plt.ylabel("GC Content(%)")
plt.title("GC content distribution along TP53 sequence)
plt.show()
