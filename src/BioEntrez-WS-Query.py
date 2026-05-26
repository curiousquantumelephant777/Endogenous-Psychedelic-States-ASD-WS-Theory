from Bio import Entrez
# Replace the placeholder domain with your email
Entrez.email = "youremail@domain.com"
databases = ["pubmed", "pmc"]

#Search multiple databases and key terms using a for loop, you could replace "Williams Syndrome" with "Autism" OR ASD"
for current_db in databases:
    query = '("Williams Syndrome" AND "GTF2I") OR ("Williams Syndrome" AND "Perineuronal Nets") OR ("Williams Syndrome" and "Layer IV/V Neurons")'

    handle = Entrez.esearch(db=current_db, term=query, retmax=7)
    record = Entrez.read(handle)
    handle.close()

    id_list = record["IdList"]
    print(f"IDs found in {current_db}: {id_list}")
