from Bio import SeqIO
import sqlExe
import gc


def round_one_classification(probe, references):
    found_records = []
    not_found_records = []
    found_flag = False
    prob_seq = SeqIO.parse(probe, 'fasta')
    # create SQL table with probe test name
    sqlExe.create_mapping_table(probe)
    # iteration over all records in probe
    for index, record in enumerate(prob_seq):
        print("Found flag:", found_flag)
        #     iteration over all references
        print("Found records:", found_records)
        for key in references.keys():
            if record.id in found_records:
                break
            found_flag = False
            # list of all chr seqs
            reference_sequences = references[key]
            reference_sequences.sort()
            #  adds column with name of the genome Name reference
            sqlExe.create_column_mapping(probe, key)
            print("References paths", reference_sequences)
            for ref_seq in reference_sequences:
                # print("Reference path:", ref_seq)
                ref_seq_fasta = SeqIO.parse(ref_seq, 'fasta')
                # all records in each chr
                # print("Path:", ref_seq)
                for ref_seq_fasta_record in ref_seq_fasta:
                    ref_seq_fasta_string = str(ref_seq_fasta_record.seq)
                    # this step is checking
                    if str(record.seq) in ref_seq_fasta_string:
                        found_flag = True
                        print("*********************")
                        print("FOUND")
                        print("Found flag:", found_flag)
                        print("Probe index:", index)
                        print("Probe seq:", record.seq)
                        print("Reference key:", key)
                        print("Reference id:", ref_seq_fasta_record.id)
                        # map found probe with id
                        break
                    else:
                        print("*********************")
                        print("NOT FOUND")
                        print("Found flag:", found_flag)
                        print("Probe index:", index)
                        print("Probe seq:", record.seq)
                        print("Reference key:", key)
                        print("Reference id:", ref_seq_fasta_record.id)
                if found_flag:
                    if record.id in not_found_records:
                        sqlExe.add_existing_row_record_to_mapping(probe, key, record.id, record.name, record.description,
                                                                  record.seq, str(ref_seq_fasta_record.id) + ' '+ ref_seq)
                    else:
                        sqlExe.add_record_to_mapping(probe, key, record.id, record.name, record.description, record.seq,
                                                 str(ref_seq_fasta_record.id) + ' ' + ref_seq)
                    found_records.append(record.id)
                    del ref_seq_fasta
                    gc.collect()
                    break
            if not found_flag:
                if record.id not in not_found_records:
                    not_found_records.append(record.id)
                    sqlExe.add_record_to_mapping(probe, key, record.id, record.name, record.description, record.seq,
                                                 "n/a")
                else:
                    sqlExe.add_existing_row_record_to_mapping(probe, key, record.id, record.name, record.description, record.seq,
                                                 "n/a")
        if not found_flag:
            del ref_seq_fasta
            gc.collect()
        if index == 10:
            break
