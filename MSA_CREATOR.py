import os

directory = os.listdir('/home/mbuyanin/Documents/KIR_MSA/FASTA')

for file in directory:
    print(file)
    os.system('../poaV2/./poa -read_fasta FASTA/' + file + ' -clustal MSA/MSA_' + file + ' ../poaV2/blosum80.mat')

