import xml.etree.ElementTree as ET
import os


tree = ET.parse('KIR.xml')
root = tree.getroot()

print(root.tag)

#with open('FASTA_Format_Alleles.txt', 'w') as fileNuc:
os.system('rm FASTA/*.txt')
for geneInfo in root:
    fileNuc = None
    geneFamily = None
    nucsequence = ""
    gensequence = ""
    formattedSequenceNuc = ""
    formattedSequenceGen = ""
    borders = []
    exonsDone = []

    KIR2DL2_KIR2DL3_Flag = 0
    KIR2DS3_KIR2DS5_Flag = 0
    KIR3DL1_KIR3DS1_Flag = 0
    KIR2DL5_Flag = 0
    #fileNuc.write("Allele Name: " + geneInfo.get('name') + '\n')
    header = ">" + geneInfo.get('name') + "\n"
    typeLocus = None
    for attributes in geneInfo:
        if str(attributes.tag).find('sequence') > -1:
            for sequence in attributes:
                #if str(sequence.tag).find('alignmentreference') > -1:
                    #fileNuc.write("Allele Name: " + sequence.get('allelename') + "\n")
                
                #fileNuc.write(sequence.tag + "\n")
                if str(sequence.tag).find('nucsequence') > -1:
                    nucsequence = sequence.text
                    #fileNuc.write("General Sequence: " + nucsequence + "\n")

                if str(sequence.tag).find('feature') > -1:
                    for information in sequence:
                        if str(information.tag).find('translation') == -1:
                            coordinateTypes = information.tag[information.tag.find('}') + 1:]
                            exonType = sequence.get('featuretype')
                            exonName = sequence.get('name')
                            if exonName not in exonsDone:
                                exonsDone.append(exonName)
                                #fileNuc.write(exonType + ": " + exonName + "\n")
                            sequenceCoordinatesStart = int(information.get('start'))
                            sequenceCoordinatesEnd = int(information.get('end'))
                            #fileNuc.write(coordinateTypes + ":\t\t")
                            if coordinateTypes.find('cDNA') > -1:
                                #fileNuc.write("\t")
                                x = 0
                            else:
                                borders.append(sequenceCoordinatesStart - 1)
                                borders.append(sequenceCoordinatesEnd)
                            #fileNuc.write(str(sequenceCoordinatesStart) + "---" + str(sequenceCoordinatesEnd) + "\n")
                                
            tempSequenceNuc = ""
            tempSequenceGen = ""
            for i in range(0, len(exonsDone)):
                rangeStart = borders[2*i]
                rangeEnd = borders[2*i + 1]
                if exonsDone[i].find('Exon') > -1 and exonsDone[i].find('Pseudo') == -1: #2i and 2i + 1
                    # KIR2DS Series incorrectly labeled in KIR.xml. Psuedoexon 3 is labeled as an Exon.
                    if typeLocus.find('KIR2DS') > -1 and exonsDone[i].find('3') > -1:
                        print('KIR.xml incorrectly labeled.')
                    else: 
                        tempSequenceNuc += nucsequence[rangeStart:rangeEnd]
                tempSequenceGen += nucsequence[rangeStart:rangeEnd]

            count = 0
            
            while count+60 <= len(tempSequenceNuc):
                formattedSequenceNuc += tempSequenceNuc[count:count+60] + "\n"
                count += 60
            formattedSequenceNuc += tempSequenceNuc[count:] + '\n'
            fileNuc.write(header + formattedSequenceNuc)

            count = 0

            while count+60 <= len(tempSequenceGen):
                formattedSequenceGen += tempSequenceGen[count:count+60] + "\n"
                count += 60
            formattedSequenceGen += tempSequenceGen[count:] + '\n'
            fileGen.write(header + formattedSequenceGen)
            
            if KIR2DL2_KIR2DL3_Flag == 1:
                with open('FASTA/COMBINATION/KIR2DL2_KIR2DL3_nuc.txt', 'a') as joint_fileNuc:
                    joint_fileNuc.write(header + formattedSequenceNuc)
                with open('FASTA/COMBINATION/KIR2DL2_KIR2DL3_gen.txt', 'a') as joint_fileGen:
                    joint_fileGen.write(header + formattedSequenceGen)
                KIR2DL2_KIR2DL3_Flag = 0
            
            if KIR2DS3_KIR2DS5_Flag == 1:
                with open('FASTA/COMBINATION/KIR2DS3_KIR2DS5_nuc.txt', 'a') as joint_fileNuc:
                    joint_fileNuc.write(header + formattedSequenceNuc)
                with open('FASTA/COMBINATION/KIR2DS3_KIR2DS5_gen.txt', 'a') as joint_fileGen:
                    joint_fileGen.write(header + formattedSequenceGen)
                KIR2DS3_KIR2DS5_Flag = 0

            if KIR3DL1_KIR3DS1_Flag == 1:
                with open('FASTA/COMBINATION/KIR3DL1_KIR3DS1_nuc.txt', 'a') as joint_fileNuc:
                    joint_fileNuc.write(header + formattedSequenceNuc)
                with open('FASTA/COMBINATION/KIR3DL1_KIR3DS1_gen.txt', 'a') as joint_fileGen:
                    joint_fileGen.write(header + formattedSequenceGen)
                KIR3DL1_KIR3DS1_Flag = 0
            
            if KIR2DL5_Flag == 1:
                with open('FASTA/COMBINATION/KIR2DL5_nuc.txt', 'a') as joint_fileNuc:
                    joint_fileNuc.write(header + formattedSequenceNuc)
                with open('FASTA/COMBINATION/KIR2DL5_gen.txt', 'a') as joint_fileGen:
                    joint_fileGen.write(header + formattedSequenceGen)
                KIR2DL5_Flag = 0

            with open('FASTA/COMBINATION/General_nuc.txt', 'a') as general_fileNuc:
                general_fileNuc.write(header + formattedSequenceNuc)
            with open('FASTA/COMBINATION/General_gen.txt', 'a') as general_fileGen:
                general_fileGen.write(header + formattedSequenceGen)
            #fileNuc.write("EXPERIMENTAL SEQUENCE:\n" + formattedSequence + "\n\n")

        if str(attributes.tag).find('locus') > -1:
            fileNuc = open('FASTA/' + attributes.get('locusname') + '_nuc.txt', 'a')
            fileGen = open('FASTA/' + attributes.get('locusname') + '_gen.txt', 'a')
            typeLocus = attributes.get('locusname')
            if attributes.get('locusname') == 'KIR2DL2' or attributes.get('locusname') == 'KIR2DL3':
                KIR2DL2_KIR2DL3_Flag = 1
            if attributes.get('locusname') == 'KIR2DS3' or attributes.get('locusname') == 'KIR2DS5':
                KIR2DS3_KIR2DS5_Flag = 1
            if attributes.get('locusname') == 'KIR3DL1' or attributes.get('locusname') == 'KIR3DS1':
                KIR3DL1_KIR3DS1_Flag = 1
            if attributes.get('locusname') == 'KIR2DL5A' or attributes.get('locusname') == 'KIR2DL5B':
                KIR2DL5_Flag = 1