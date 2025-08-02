from Bio import Entrez, SeqIO
from Bio.SeqUtils import gc_fraction

def fetch_fasta(accession_id, filename="sequence.fasta"):
    Entrez.email = "your@email.com"  # Replace with your email or a throwaway email
    try:
        with Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text") as handle:
            with open(filename, "w") as out_handle:
                out_handle.write(handle.read())
        print("✅ Saved FASTA as", filename)
    except Exception as e:
        print("❌ Error fetching from NCBI:", e)

def analyze_fasta(filename="sequence.fasta"):
    try:
        record = SeqIO.read(filename, "fasta-pearson")
        seq = record.seq
        print("\n📊 Sequence Analysis:")
        print(f"ID: {record.id}")
        print(f"Length: {len(seq)} bases")
        print(f"GC Content: {gc_fraction(seq) * 100:.2f}%")
        print(f"A: {seq.count('A')}  T: {seq.count('T')}")
        print(f"G: {seq.count('G')}  C: {seq.count('C')}")
    except Exception as e:
        print("❌ Error reading FASTA:", e)

if __name__ == "__main__":
    print("🔬 NCBI DNA Fetcher")
    accession = input("Enter NCBI accession ID (e.g., NC_000852): ")
    fetch_fasta(accession)
    analyze_fasta()