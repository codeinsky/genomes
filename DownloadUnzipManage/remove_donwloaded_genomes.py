import os
import gzip
import shutil


def delete():
    # list to store txt files
    genomes = []

    # Collects all files with .gz extension
    for root, dirs, files in os.walk("./refseq"):
        for file in files:
            if file.endswith(".fna"):
                genomes.append(os.path.join(root, file))
    print(genomes)


delete()