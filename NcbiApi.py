# https://dmnfarrell.github.io/bioinformatics/assemblies-genbank-python
# download
# ncbi-genome-download --taxids 9685 --formats fasta --assembly-level chromosome all
#  ncbi-genome-download --taxids 9606,9685 --assembly-level chromosome vertebrate_mammalian
#  https://github.com/kblin/ncbi-genome-download
#  list of genoomes with ID https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/IDS/
import ncbi_genome_download as ngd
from Bio import Entrez
Entrez.email = "todorov@bezeqint.net"  # Always tell NCBI who you are
handle = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
print(handle.read())

