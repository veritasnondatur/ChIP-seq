# ChIP-seq
This script serves to construct randomized peak shifts for ChIP-seq peaks

Input: ChIP-seq peaks in .bed (.txt)

Output:

    Cleaned input file (removed random peaks that are not on chr1-19, X or Y) in .bed (or .txt)
    Randomly shifted ChIP-seq peaks in .bed (.txt)

Note on implementation: Ideally, script should not only be applied once but multiple (e.g. 1000x?) times, in order to compute randomized background and followed by overlap with bedtools intersect

Author: Vera Laub

Last Edited: 2022-11-09
