# RNA Splicing (Rosalind Bioinformatics Problem)

This project solves the **RNA Splicing** problem, where the goal is to extract exons from a DNA sequence, transcribe it into RNA, and translate it into a protein.

---

## Problem Description

Given:

- A DNA string `s` (length ≤ 1 kbp)
- A collection of substrings of `s` (introns), all provided in **FASTA format**

Return:

- A **protein string** resulting from transcribing and translating the exons of `s` (i.e., the original string minus all introns).

---

## Example Input (`input.txt`)

```
>Rosalind_10  
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG  
>Rosalind_12  
ATCGGTCGAA  
>Rosalind_15  
ATCGGTCGAGCGTGT
```

---

## Sample Output

```
MVYIADKQHVASREAYGHMFKVCA*
```

---

## How to Run

### 1. Requirements

- Python 3
- Biopython

Install Biopython:

```bash
pip install biopython
```

### 2. Run the Script

Make sure you have your `input.txt` in the same folder, then:

```bash
python rna_splicing.py
```

---

## Project Structure

```
.
├── input.txt           # Input FASTA file with DNA + introns
├── rna_splicing.py     # Main script to solve the problem
└── README.md           # You are here!
```

---

## What It Does 

1. Parses the FASTA file
2. Identifies the full DNA and introns
3. Removes all introns from the DNA
4. Transcribes DNA → RNA
5. Translates RNA → Protein

---

## Resources

- [Rosalind Info](http://rosalind.info/problems/splc/)
- [Biopython Docs](https://biopython.org/wiki/Documentation)

---

