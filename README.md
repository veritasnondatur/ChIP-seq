## ChIP-seq
Collection of small programs to be used for ChIP-seq analysis.



#Program name: randomized_peak_shift

This script serves to construct randomized peak shifts for ChIP-seq peaks.

Input: ChIP-seq peaks in .bed (.txt)

Output:
1. Cleaned input file (removed random peaks that are not on chr1-19, X or Y) in .bed (or .txt)
2. Randomly shifted ChIP-seq peaks in .bed (.txt)

Note on implementation: Ideally, script should not only be applied once but multiple (e.g. 1000x?) times, in order to compute randomized background and followed by overlap with bedtools intersect

Author: Vera Laub
Last Edited: 2022-11-09



#Program name: chip-seq_rna-seq_peak_collection

This program serves the purpose of assembling Genes from an RNA-seq file (1. Input) and collecting the respective ChIP-seq peaks (2. Input), i.e. PBX1 ChIP-seq peaks of genes that are differentially regulated in Pbx1 kd RNA-seq in aNS cells (but can be used on any kind of ChIP/RNA-seq, if necessary data is provided). Code meant to be flexible :)!

Input: .txt with RNA-Seq data (ENSEMBLE ID, Gene ID, Fold change), .txt files with ChIP-seq data (Gene ID, peak chr, peak start, peak stop, summit chr, summit start, summit stop)

Output: .bed file with ChIP-seq peaks of all genes defined in RNA-seq file (peak chr, peak start, peak stop, Gene ID)

Author: Vera Laub
Last Edited: 2023-02-20

