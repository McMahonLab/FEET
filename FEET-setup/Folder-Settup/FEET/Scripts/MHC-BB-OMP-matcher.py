''' 
this python script searches an bin_or_MAG.faa file from prodigal anotation output for a given protein such as an MHC 
and looks plus or minus X proteins (sequentially) and asks if a protein from another file is in there. 

MHC-BB-OMP-matcher.py <protein 1> <protein 2> <faa file for the proteins> <X>
where
protein 1 = protein around which you want to know protein 2 is.
faa file for file 1 and 2 = faa in prodigal format with ID=X_Y in the 9th field of the annotation
protein 2 = protein which you want to know if it's within X proteins away from protein 1
X = how many proteins it could be away and be considered 'near'
output file format: protein 1,protein 2\n (only if they're found near each other, within Thresh)
'''

import sys
import os
import re

if sys.argv[1] == []:
	print('Usage:')
	print(argv[0] + 'Protein_1 FaaFile Protein_2 MaxORFsAway')

Protein_1 = str(sys.argv[1])
Protein_2 = str(sys.argv[2])
FaaFile = sys.argv[3]
Thresh = int(sys.argv[4])
FaaName = str(FaaFile).split("/")[-1].strip().split(".fna")[0].strip()

#OrfNum1 =
#ScafNum1 = 
with open(FaaFile,'r') as reading:
    jam = 0
    for line in reading:
        if re.search(Protein_1,line) and jam == 0:
            ScafNum1 = line.split(" ")[8].strip().split(";")[0].strip().split("=")[1].strip().split("_")[0].strip()
            OrfNum1 = line.split(" ")[8].strip().split(";")[0].strip().split("=")[1].strip().split("_")[1].strip()
            jam = 1
#print("Protein_1 is ORF number " + OrfNum1 + " in scaffold number " + ScafNum1)

with open(FaaFile,'r') as reading:
    jam = 0
    for line in reading:
        if re.search(Protein_2,line) and jam == 0:
            ScafNum2 = line.split(" ")[8].strip().split(";")[0].strip().split("=")[1].strip().split("_")[0].strip()
            OrfNum2 = line.split(" ")[8].strip().split(";")[0].strip().split("=")[1].strip().split("_")[1].strip()
            jam = 1
#print("Protein_2 is ORF number " + OrfNum2 + " in scaffold number " + ScafNum2)

if ScafNum1 == ScafNum2:
    if int(OrfNum2) <= int(OrfNum1) + Thresh and int(OrfNum2) >= int(OrfNum1) - Thresh:
        print(FaaName + "," + Protein_1 + "," + Protein_2)
        
        