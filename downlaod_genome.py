import os


def download_genome(genome_id):
    command = "ncbi-genome-download --taxids " + str(genome_id) + " --formats fasta --assembly-level chromosome all"
    print(command)
    os.system(command)
    print("download done")


