import sys

from loadProbesOld import load_probes_fasta_files
from loadReferncesGenomesOld import load_reference_genomes
from OldTests.roundOneClassificationOld import round_one_classification

# start_time = time.time()
sys.path.append("..")
probes = load_probes_fasta_files()
references = load_reference_genomes()
for probe in probes:
    # creates main table for probe results
    round_one_classification(probe, references)
# print("Time results", time.time() - start_time)
