"""This program serves to find genes that are bound by PBX1 in several
locations. To find respective genes, the annotations to both strands
are used and saved in two separate output dicionaries.
INPUT: .csv file from PBX1 ChIP-Seq
OUTPUT: Dictionary, counting the number of peaks for each gene that are bound
    by PBX1 is listed.
VERSION: 2019-12-03, initialize program
AUTHOR: Vera Laub
INFO: https://www.youtube.com/watch?v=vmEHCJofslg
      https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

"""

import pandas as pd


# Get input file (PBX1 ChIP-Seq peaks)
raw_data = 'chip-seq_pbx1_peaks.csv'
peaks_total = pd.read_csv(raw_data, delimiter = '\t')


# Create list of gene.id_1 and gene.id_1 entries with all peaks
gene_id_1 = peaks_total['gene.id_1'].tolist()
gene_id_2 = peaks_total['gene.id_2'].tolist()


# Count amount of peaks for every annotated gene and store in dict
def count_peaks(gene_id_1, gene_id_2):
    """Store gene names annotated to peaks from the two lists in dictionary
    and count number of occurences in dataset.

    """
    n_peaks_per_gene = {} # Create empty dictionary 1 (for gene.id_1)
    for gene in gene_id_1:
        if gene not in n_peaks_per_gene:
            n_peaks_per_gene[str(gene)] = 1
        elif gene in n_peaks_per_gene:
            n_peaks_per_gene[str(gene)] += 1
    return n_peaks_per_gene
    
counted_peaks = count_peaks(gene_id_1, gene_id_2) # Output 1: dictionary


# Extract genes with many peaks

# 100+
def get_keys_by_value(counted_peaks, value_to_find):
    '''
    Get a list of genes from dictionary which has the given peak count
    '''
    list_of_keys = list()
    list_of_items = counted_peaks.items()
    for item  in list_of_items:
        if item[1] >= value_to_find:
            list_of_keys.append(item[0])
    return list_of_keys

list_of_keys = get_keys_by_value(counted_peaks, 100)
print("Genes with 100+ peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)


def get_keys_by_value_range(counted_peaks, first_value, last_value):
    '''
    Get a list of keys from dictionary which is in the range of two given
    values.
    '''
    list_of_keys = list()
    list_of_items = counted_peaks.items()
    for item  in list_of_items:
        if item[1] >= first_value and item[1] <= last_value:
            list_of_keys.append(item[0])
    return list_of_keys


# 90-99
list_of_keys = get_keys_by_value_range(counted_peaks, 90, 99)
print("Genes with 90-99 peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)


# 80-89
list_of_keys = get_keys_by_value_range(counted_peaks, 80, 89)
print("Genes with 80-89 peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)

        
# 70-79
list_of_keys = get_keys_by_value_range(counted_peaks, 70, 79)
print("Genes with 70-79 peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)

        
# 60-69
list_of_keys = get_keys_by_value_range(counted_peaks, 60, 69)
print("Genes with 60-69 peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)

        
# 50-59
list_of_keys = get_keys_by_value_range(counted_peaks, 50, 59)
print("Genes with 50-59 peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)
        

# 40-49
list_of_keys = get_keys_by_value_range(counted_peaks, 40, 49)
print("Genes with 40-49 peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)


# 30-39
list_of_keys = get_keys_by_value_range(counted_peaks, 30, 39)
print("Genes with 30-39 peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)


# 20-29
list_of_keys = get_keys_by_value_range(counted_peaks, 20, 29)
print("Genes with 20-29 peaks: ")

#Iterate over the list of keys
for key  in list_of_keys: 
        print(key)


# 10-19
#list_of_keys = get_keys_by_value(counted_peaks, 10, 19)
#print("Genes with 10-19 peaks: ")

#Iterate over the list of keys
#for key  in list_of_keys: 
#        print(key)

        
# 1-9
#list_of_keys = get_keys_by_value(counted_peaks, 1, 9)
#print("Genes with 1-9 peaks: ")

#Iterate over the list of keys
#for key  in list_of_keys: 



# Output 2: Histogram representing amounts of peaks per genes
# Do the same for gene.id_2
