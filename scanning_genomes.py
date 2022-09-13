from Bio import SeqIO
import os
from SQLexe import sqlExe
import gc


def scan_genomes(ref_genomes, probe):
    print(ref_genomes)
    print(probe)
    # Loading probe in fasta class
    prob_seq = SeqIO.parse(probe, 'fasta')
    # Loading references
    references_genomes_files = load_genomes_paths(ref_genomes)
    # create mapping table
    sqlExe.create_mapping_table(probe)
    # Loop over probes
    for index, record in enumerate(prob_seq):
        flag_found = False
        # loop over reference
        for index_ref, (key, value) in enumerate(references_genomes_files.items()):
            if flag_found:
                break
            #  creates SQL column column for reference genome
            sqlExe.create_column_mapping(probe, key)
            print("Probe description", record.description)
            print("Probe seq", record.seq)
            print("Reference:", key)
            # print("Path", value)
            ref_seq = SeqIO.parse(value, 'fasta')
            print("Reference genome")
            for i, ref_record in enumerate(ref_seq):
                print(ref_record.id)
                if str(record.seq) in str(ref_record.seq).upper():
                    print("Found:", ref_record.id)
                    sqlExe.add_record_to_mapping(probe, key, record.id, record.name, record.description, record.seq,
                                                 ref_record.id)
                    flag_found = True
                    break
            print(index_ref, " of ", len(references_genomes_files))
            # record checked for all references and not found
            if index_ref == len(references_genomes_files) - 1:
                sqlExe.add_record_to_mapping(probe, key, record.id, record.name, record.description, record.seq,
                                             '')
                print('Not Found')

        if index == 100:
            break
        gc.collect()


def load_genomes_paths(ref_genomes):
    ref_gens = {}
    for gen in ref_genomes:
        for root, dirs, files in os.walk("./refseq"):
            for name in files:
                if name == gen:
                    ref_gens[gen] = os.path.abspath(os.path.join(root, name))
    return ref_gens
