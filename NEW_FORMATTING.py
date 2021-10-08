import os
import re

directory = os.listdir('/home/mbuyanin/Documents/KIR_MSA/MSA/')
tempdirectory = os.listdir('/home/mbuyanin/Documents/KIR_MSA/MSA/TEMP_FILES/')
os.system('rm MSA/MY_FORMAT/*')

sequences = ['KIR2DL1', 'KIR2DL2', 'KIR2DL3', 'KIR2DL4', 'KIR2DL5A', 'KIR2DL5B', 'KIR2DS1', 'KIR2DS2', 'KIR2DS3', 'KIR2DS4', 'KIR2DS5', 'KIR2DP1', 'KIR3DL1', 'KIR3DL2', 'KIR3DL3', 'KIR3DS1', 'KIR3DP1']

for file in directory: #One file
    dict_seq = {}
    count = 0
    if file.startswith('MSA_'):
        #print(file[4:])
        with open('MSA/' + file, 'r') as clustalw:
            line = clustalw.readline()
            line = clustalw.readline()
            line = clustalw.readline()
            for line in clustalw:
                if line != '\n':
                    gap = line.find(' ')
                    seqName = line[:gap].strip()
                    seqInfo = line[gap:].strip()
                    if seqName not in dict_seq:
                        dict_seq[seqName] = seqInfo
                    else:
                        dict_seq[seqName] += seqInfo
                    #with open('MSA/TEMP_FILES/' + file[4:-4] + '/' + seqName, 'a') as tempFile:
                    #    tempFile.write(seqInfo)
            #print(dict_seq)
                
            print(file[4:])

            with open('MSA/MY_FORMAT/FORMAT_' + file[4:], 'a') as myFile:
                for entry in dict_seq:
                    myFile.write(entry + '\t\t' + dict_seq[entry] + '\n')