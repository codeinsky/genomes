import os


def load_reference_genomes():
    reference_folder = './ReferenceGenomes'
    reference_sub_folder = os.listdir(reference_folder)
    references_data = {}
    for folder in reference_sub_folder:
        reference_list = []
        chr_folders = os.listdir(reference_folder + "/" + folder)
        # print(chrFolders)
        for chr_folder in chr_folders:
            chr_files = os.listdir(reference_folder + "/" + folder + "/" + chr_folder)
            for file in chr_files:
                file = reference_folder + "/" + folder + "/" + chr_folder + "/" + file
                reference_list.append(file)
        references_data[folder] = reference_list
    return references_data

