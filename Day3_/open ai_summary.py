from Bio import Entrez
from openai import OpenAPI
client = OpenAI(api_key=" YOUR API KEY")
entrez.email = "your@gmail.com"
# Step 1: Search Pubmed
handle = Entrez.esearch(
    db="pubmed",
    term="TP53 cancer mutation",
    retmax=5
)
record = Entrez.read(handle)
ids = record["IdList"]

print(ids)

# Step 2: Fetch abstracts
handle = Entrez.efetch(
    db="pubmed",
    id=ids,
    rettype="abstract",
    retmode="text"
)
# NOW handle exists
abstracts = handle.read()
You are a bioinformatics assistant.

Summarize into:
1. Biological Function
2. Disease Relevance
3. Research Applications
4. Clinical Relevance
{abstracts}
"""

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"user","content":prompt}
)
print(response.choices[0].message.content)
