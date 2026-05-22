# Day 3: PubMed litreature mining using Biopython Entrez API
from Bio import Entrez
Entrez.email = "your@gmail.com"  # Required by NCBI
# Step 1: Search PubMed
handle = Entrez.esearch(
  db="pubmed",
  term="TP53 Cancer mutation",
  retmax=5
)
record = Entrez.read(handle)
ids = record["IDList"]
print("Article IDs found:", ids)
#Step 2: Fetch abstracts
handle = Entrez.efetch(
  db="pubmed",
  id=ids,
  rettype="abstract",
  retmode="text"
)
abstracts = handle.read()
print(abstracts)
