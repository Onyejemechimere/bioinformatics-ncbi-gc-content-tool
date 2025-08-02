# bioinformatics-ncbi-gc-content-tool
A Python script to fetch DNA sequences from NCBI, analyze GC content, and visualize base counts.
This is a simple Python script I wrote to help fetch DNA sequences from NCBI using their accession ID, save them as a FASTA file, and analyze basic stats like GC content and base counts.

I built it to practice bioinformatics skills using Biopython, and to solve a real-world task for beginner-level sequence analysis.

## What It Does

- Takes an NCBI accession ID as input (like `NC_000852`)
- Fetches the DNA sequence and saves it as a `.fasta` file
- Analyzes the sequence:
  - Length of the sequence
  - GC content (percentage of G and C bases)
  - Count of A, T, G, C bases

---

##  Requirements

Make sure Python is installed. Then install Biopython:

```bash
pip install biopython
