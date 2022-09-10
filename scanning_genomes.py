from Bio import SeqIO
import os


def scan_genomes(ref_genomes, probe):
    print(ref_genomes)
    print(probe)
    # Loading probe in fasta class
    prob_seq = SeqIO.parse(probe, 'fasta')
    # Loading references
    references_genomes_files = load_genomes_paths(ref_genomes)
    # Loop over probes
    for index, record in enumerate(prob_seq):
        for key, value in references_genomes_files.items():
            print("Probe description", record.description)
            print("Probe seq", record.seq)
            print("Reference:", key)
            print("Path", value)
            ref_seq = SeqIO.parse(value, 'fasta')
            print("Reference genome")
            for ref_record in ref_seq:
                print(ref_record.id)
        if index == 0:
            break


def load_genomes_paths(ref_genomes):
    ref_gens = {}
    for gen in ref_genomes:
        for root, dirs, files in os.walk("./refseq"):
            for name in files:
                if name == gen:
                    ref_gens[gen] = os.path.abspath(os.path.join(root, name))
    return ref_gens
