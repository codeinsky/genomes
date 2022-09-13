import os
import gzip
import shutil


def unzip():
    # list to store txt files
    res_archives = []

    # Collects all files with .gz extension
    for root, dirs, files in os.walk("./refseq"):
        for file in files:
            if file.endswith(".gz"):
                res_archives.append(os.path.join(root, file))

    # unzip all .gz files
    for archive in res_archives:
        with gzip.open(archive, 'rb') as f_in:
            file_name = archive.replace(".gz", '')
            with open(file_name, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    # delete all archive files
    for file in res_archives:
        os.remove(file)
