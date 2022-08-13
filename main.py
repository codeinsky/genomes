import sys
import time

from loadProbes import load_probes_fasta_files
from loadReferncesGenomes import load_reference_genomes
from roundOneClassification import round_one_classification

# start_time = time.time()
sys.path.append(".")
probes = load_probes_fasta_files()
references = load_reference_genomes()
for probe in probes:
    # creates main table for probe results
    round_one_classification(probe, references)
# print("Time results", time.time() - start_time)
