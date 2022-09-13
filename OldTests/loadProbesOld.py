import os


def load_probes_fasta_files():
    probes = []
    probes_folder = './Probes/'
    probes_sub_folders = os.listdir(probes_folder)
    for folder in probes_sub_folders:
        files = os.listdir(probes_folder + folder)
        for file in files:
            probes.append(probes_folder + str(folder) + "/" + file)
    return probes

