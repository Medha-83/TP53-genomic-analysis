# TP53-genomic-analysis
Genomic analysis pipeline for TP53 gene: GC content, ORF annotation, and AI-assisted litreature interpretation using Biopython and Entrez API.
# Objective
To build a reproducible, end-to-end pipeline that takes a raw gene sequence as input and produces a complete biological report covering sequence statistics, feature annotation, and litreature-based interpretation
# Tools used
Python 3.14 | BioPython | Matplotlib | NCBI Entrez API | Claude AI
# How to run
a) Install dependencies: "pip install biopython matplotlib"
b) Download TP53 FASTA from NCBI (NM_000537.3)
c) Run: python "pipeline.py --fasta tp53.fasta --gene TP53"
d) Output saved to: "tp53_reprot.txt" + "gc_plot.png"
# Results
Sequence length: 2591bp | GC Content: 47.32%
ORFs found: 4 | Longest ORF: 1182bp (position 203-1385)
Key finding: Peak GC content overlaps directly with the dominant coding ORF
# Acknowledements
Built during the "Bversity Computational Biology Workshop", May 2026.
Mentored by Jeevitha C M 
