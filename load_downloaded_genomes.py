import os


def load_downloaded_genomes():
    res_archives = []
    genomes = []
    # Collects all files with .gz extension
    for root, dirs, files in os.walk("./refseq"):
        for file in files:
            if file.endswith(".fna"):
                res_archives.append(os.path.join(root, file))

    if len(res_archives) > 0:

        genomes = [gen.split("/")[-1] for gen in res_archives]
    return genomes
