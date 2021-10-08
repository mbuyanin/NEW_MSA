import os

directory = os.listdir('/home/mbuyanin/Documents/KIR_MSA/MSA')

HLA_TYPES = ['A', 'B', 'C', 'DMA', 'DMB', 'DOA', 'DPA1', 'DPB1', 'DPB2', 'DQA1', 'DQB1', 'DRA', 'DRB1', 'DRB2', 'DRB3', 'DRB4', 'DRB5', 'DRB6', 'DRB7', 'DRB8', 'DRB9', 'E', 'F', 'G', 'HFE', 'H', 'J', 'K', 'L', 'MICA', 'MICB', 'TAP1', 'TAP2', 'V', 'Y']

for type in HLA_TYPES:
    os.system('touch MSA/RENAMED/' + type + '_gen.txt')
    os.system('touch MSA/RENAMED/' + type + '_nuc.txt')

for file in directory:
    if file.find('2DL1') > -1:
        os.system('cp MSA/MSA_KIR2DL1_gen.txt MSA/RENAMED/A_gen.txt')
        os.system('cp MSA/MSA_KIR2DL1_nuc.txt MSA/RENAMED/A_nuc.txt')
    if file.find('2DL2') > -1:
        os.system('cp MSA/MSA_KIR2DL2_gen.txt MSA/RENAMED/B_gen.txt')
        os.system('cp MSA/MSA_KIR2DL2_nuc.txt MSA/RENAMED/B_nuc.txt')
    if file.find('2DL3') > -1:
        os.system('cp MSA/MSA_KIR2DL3_gen.txt MSA/RENAMED/C_gen.txt')
        os.system('cp MSA/MSA_KIR2DL3_nuc.txt MSA/RENAMED/C_nuc.txt')
    if file.find('2DL4') > -1:
        os.system('cp MSA/MSA_KIR2DL4_gen.txt MSA/RENAMED/E_gen.txt')
        os.system('cp MSA/MSA_KIR2DL4_nuc.txt MSA/RENAMED/E_nuc.txt')
    if file.find('2DL5A') > -1:
        os.system('cp MSA/MSA_KIR2DL5A_gen.txt MSA/RENAMED/F_gen.txt')
        os.system('cp MSA/MSA_KIR2DL5A_nuc.txt MSA/RENAMED/F_nuc.txt')
    if file.find('2DL5B') > -1:
        os.system('cp MSA/MSA_KIR2DL5B_gen.txt MSA/RENAMED/G_gen.txt')
        os.system('cp MSA/MSA_KIR2DL5B_nuc.txt MSA/RENAMED/G_nuc.txt')
    if file.find('2DS1') > -1:
        os.system('cp MSA/MSA_KIR2DS1_gen.txt MSA/RENAMED/H_gen.txt')
        os.system('cp MSA/MSA_KIR2DS1_nuc.txt MSA/RENAMED/H_nuc.txt')
    if file.find('2DS2') > -1:
        os.system('cp MSA/MSA_KIR2DS2_gen.txt MSA/RENAMED/J_gen.txt')
        os.system('cp MSA/MSA_KIR2DS2_nuc.txt MSA/RENAMED/J_nuc.txt')
    if file.find('2DS3') > -1:
        os.system('cp MSA/MSA_KIR2DS3_gen.txt MSA/RENAMED/K_gen.txt')
        os.system('cp MSA/MSA_KIR2DS3_nuc.txt MSA/RENAMED/K_nuc.txt')
    if file.find('2DS4') > -1:
        os.system('cp MSA/MSA_KIR2DS4_gen.txt MSA/RENAMED/L_gen.txt')
        os.system('cp MSA/MSA_KIR2DS4_nuc.txt MSA/RENAMED/L_nuc.txt')
    if file.find('2DS5') > -1:
        os.system('cp MSA/MSA_KIR2DS5_gen.txt MSA/RENAMED/DRA_gen.txt')
        os.system('cp MSA/MSA_KIR2DS5_nuc.txt MSA/RENAMED/DRA_nuc.txt')
    if file.find('2DP1') > -1:
        os.system('cp MSA/MSA_KIR2DP1_gen.txt MSA/RENAMED/V_gen.txt')
        os.system('cp MSA/MSA_KIR2DP1_nuc.txt MSA/RENAMED/V_nuc.txt')
    if file.find('3DP1') > -1:
        os.system('cp MSA/MSA_KIR3DP1_gen.txt MSA/RENAMED/Y_gen.txt')
        os.system('cp MSA/MSA_KIR3DP1_nuc.txt MSA/RENAMED/Y_nuc.txt')
    if file.find('3DL1') > -1:
        os.system('cp MSA/MSA_KIR3DL1_gen.txt MSA/RENAMED/DMA_gen.txt')
        os.system('cp MSA/MSA_KIR3DL1_nuc.txt MSA/RENAMED/DMA_nuc.txt')
    if file.find('3DL2') > -1:
        os.system('cp MSA/MSA_KIR3DL2_gen.txt MSA/RENAMED/DMB_gen.txt')
        os.system('cp MSA/MSA_KIR3DL2_nuc.txt MSA/RENAMED/DMB_nuc.txt')
    if file.find('3DL3') > -1:
        os.system('cp MSA/MSA_KIR3DL3_gen.txt MSA/RENAMED/DOA_gen.txt')
        os.system('cp MSA/MSA_KIR3DL3_nuc.txt MSA/RENAMED/DOA_nuc.txt')
    if file.find('3DS1') > -1:
        os.system('cp MSA/MSA_KIR3DS1_gen.txt MSA/RENAMED/MICA_gen.txt')
        os.system('cp MSA/MSA_KIR3DS1_nuc.txt MSA/RENAMED/MICA_nuc.txt')