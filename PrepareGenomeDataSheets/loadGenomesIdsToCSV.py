import pandas as pd
import glob


def textDataSheetToCSV():
    genome_id_files = glob.glob("./genomeIds/*")
    for file_name in genome_id_files:
        file_name_str = file_name.split('/')[2].split('.')[0]
        print("file name is:", file_name_str)
        columns = ['id', 'chr', 'number', 'flag', 'code', 'desc']
        data_genomes = pd.DataFrame(columns=columns)
        with open(file_name) as file:
            for index, line in enumerate(file):
                # print(line)
                row_list = ' '.join(line.split()).split(' ')
                # print(' '.join(line.split()).split(' '))
                genome_id = row_list[0]
                genome_chr = row_list[1]
                genome_number = row_list[2]
                genome_flag = row_list[3]
                genome_code = row_list[4]
                genome_desc = ' '.join(row_list[5:])
                row_obj = {
                    "id": genome_id,
                    "chr": genome_chr,
                    "number": genome_number,
                    "flag": genome_flag,
                    "code": genome_code,
                    "desc": genome_desc
                }
                data_genomes = data_genomes.append(row_obj, ignore_index=True)
                # if index == 1:
                #     break
        data_genomes.to_csv("./genomeIdCsv/" + file_name_str + '.csv')
        print("Failed saved:", file_name_str)


