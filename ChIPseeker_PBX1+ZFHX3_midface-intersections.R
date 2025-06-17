### Script to compute annotation of ChIP-seq datasets using ChIP-seeker
# Author: Vera Laub
# Date last edited: 06/17/2025
# Input: .bed file of ChIP-seq peaks
# Output: Annotation of dataset

# Load libraries
library(ChIPseeker)
library(TxDb.Mmusculus.UCSC.mm10.knownGene)
library(org.Mm.eg.db)

# Run Analysis

# Define reference
txdb <- TxDb.Mmusculus.UCSC.mm10.knownGene

# Analysis of intersecting PBX1 peak summits E11.5 MF (Marta) with all three ZFHX3 E11.5 midface datasets (Tony)
peaks_PBX1+ZFHX3_intersections <- readPeakFile("/Users/veralaub/Documents/postdoc/bioinformatics/results/online_tools/bedtools/bedtools_multiinter_PBX1+ZFHX3_midface/2025-06-17_bedtools_multiinter_ChIP-seq_PBX1+ZFHX3_E11.5_excludingEmptyRegions.bed")

peakAnno_PBX1+ZFHX3_intersections <- annotatePeak(peaks_PBX1+ZFHX3_intersections, TxDb = txdb, annoDb = "org.Mm.eg.db")

plotAnnoPie(peakAnno_PBX1+ZFHX3_intersections)


# Analysis of individual PBX1 peak summits E11.5 MF (Marta) and all three ZFHX3 E11.5 midface datasets (Tony)
peaks_PBX1 <- readPeakFile("/Users/veralaub/Documents/postdoc/bioinformatics/data/ChIP-seq/midface/MF_ip_pbx_vs_input_11_summits.bed")
peakAnno_PBX1 <- annotatePeak(peaks_PBX1, TxDb = txdb, annoDb = "org.Mm.eg.db")
plotAnnoPie(peakAnno_PBX1)

peaks_ZFHX3_rep1 <- readPeakFile("/Users/veralaub/Documents/postdoc/bioinformatics/data/ChIP-seq/midface/E115-ZFHX3_1_peaks.bed")
peakAnno_ZFHX3_rep1 <- annotatePeak(peaks_ZFHX3_rep1, TxDb = txdb, annoDb = "org.Mm.eg.db")
plotAnnoPie(peakAnno_ZFHX3_rep1)

peaks_ZFHX3_rep2 <- readPeakFile("/Users/veralaub/Documents/postdoc/bioinformatics/data/ChIP-seq/midface/E115-ZFHX3_2_peaks.bed")
peakAnno_ZFHX3_rep2 <- annotatePeak(peaks_ZFHX3_rep2, TxDb = txdb, annoDb = "org.Mm.eg.db")
plotAnnoPie(peakAnno_ZFHX3_rep2)

peaks_ZFHX3_rep3 <- readPeakFile("/Users/veralaub/Documents/postdoc/bioinformatics/data/ChIP-seq/midface/E115-ZFHX3_3_peaks.bed")
peakAnno_ZFHX3_rep3 <- annotatePeak(peaks_ZFHX3_rep3, TxDb = txdb, annoDb = "org.Mm.eg.db")
plotAnnoPie(peakAnno_ZFHX3_rep3)
