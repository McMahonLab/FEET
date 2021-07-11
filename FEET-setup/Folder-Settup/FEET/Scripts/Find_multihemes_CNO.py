#! /usr/bin/python

'''
This script prints the list of sequences with at least n heme-binding motif "C..CH".
It requires two inputs. The first input is the file you'd like to search, and the
second is the minimum number of heme-binding sites required to include an ORF.
'''

import sys
import os
import re
from Bio import SeqIO

infile = sys.argv[1]

if sys.argv[1] == []:
	print('Usage:')
	print(argv[0] + 'Infile')

nstring = sys.argv[2]
n = int(nstring)
#input number of C..CH hemes to move onto searching for more hemes, recommend: 3 
nstring = sys.argv[3]
cutoff = int(nstring)
#input minimum number of any hemes to be counted as a multiheme protein, recommend: 5 to be more likely to be EET evidence downstream

heme = re.compile(r"C..CH")
hem1 = re.compile(r"C.CH")
hem3 = re.compile(r"C...CH")
hem4 = re.compile(r"C...........[!=C]..CH")

seq_record = list(SeqIO.parse(infile,"fasta"))

i = 0

parentfolder = os.path.dirname(os.path.dirname(infile))
if not os.path.exists('%s/MHCs/' % (parentfolder)):
    os.makedirs('%s/MHCs/' % (parentfolder))
outfolder = '%s/MHCs/' % (parentfolder)

outfile1 = outfolder + os.path.basename(infile.split('.')[0] + '_' + str(n) + '_heme_count.txt')
outfile2 = outfolder + os.path.basename(infile.split('.')[0] + '_' + str(n) + '_heme_list.txt')
outfile3 = outfolder + os.path.basename(infile.split('.')[0] + '_' + str(n) + '_heme.faa')

with open(outfile1, 'w') as f:
	with open(outfile2, 'w') as f2:
		with open(outfile3, 'w') as f3:
			f.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format('gene_oid', 'Num_of_C..CH', 'Num_of_C.CH', 'Num_of_C...CH', 'Num_of_C...........[!=C]..CH', 'Total_Num_of_heme'))
			for seq in SeqIO.parse(infile,'fasta'):
				heme_sites = re.findall(heme, str(seq.seq))
				if len(heme_sites) >= n:
					hem1_sites = re.findall(hem1, str(seq.seq))
					hem3_sites = re.findall(hem3, str(seq.seq))
					hem4_sites = re.findall(hem4, str(seq.seq))
					total_heme = len(heme_sites) + len(hem1_sites) + len(hem3_sites) + len(hem4_sites)
					if total_heme >= cutoff:
						i+=1
						f.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n'.format(seq.id, len(heme_sites), len(hem1_sites), len(hem3_sites), len(hem4_sites), total_heme))
						f2.write('{0}\n'.format(seq.id))
						f3.write('>{0}\n'.format(seq.id) + '{0}\n'.format(seq.seq))

print('\nThere are %i sequences and %i of them have at least %i heme-binding sites.' % (len(seq_record), i, cutoff))
print('The results is printed to %s and %s and %s.\n' % (outfile1, outfile2, outfile3))
