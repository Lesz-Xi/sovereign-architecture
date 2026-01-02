import math
from collections import Counter

def calculate_shannon_entropy(sequences):
    """
    Calculates Shannon Entropy for each position in an alignment.
    Iterates through columns. Ignores gaps ('-').
    H(X) = - sum(p(x) * log2(p(x)))
    """
    if not sequences:
        return []

    seq_length = len(sequences[0])
    num_sequences = len(sequences)
    entropies = []
    
    # Iterate through each column (position)
    for i in range(seq_length):
        column_residues = []
        for seq in sequences:
            # We must handle the case where sequences might be different lengths
            # if the file is malformed, but this is a pre-aligned file.
            if i < len(seq):
                residue = seq[i]
                # Filter out gaps and non-standard AA if necessary.
                # Standard alignment gaps are '-' or '.'
                if residue not in ['-', '.', '?', '*']: 
                    column_residues.append(residue)
        
        # If a column is ALL gaps, entropy is technically 0 (no information), 
        # but for our purpose it's "undefined" or "ignore". 
        # Let's verify if we want to flag it as Conserved (Entropy 0) or Invalid.
        # An all-gap column means "this position doesn't exist in most viruses".
        # We only care about positions that EXIST and are CONSERVED.
        
        if not column_residues:
            entropies.append(None) 
            continue

        # CRITICAL FIX: GAP FILTERING
        # If the column is mostly gaps, it is not "Conserved", it is "Absent".
        # We enforce that at least 50% of sequences must have a residue here.
        occupancy = len(column_residues) / num_sequences
        if occupancy < 0.50:
            entropies.append(None) # Too many gaps, ignore
            continue

        total_residues = len(column_residues)
        counts = Counter(column_residues)
        
        entropy = 0.0
        for residue, count in counts.items():
            probability = count / total_residues
            entropy -= probability * math.log2(probability)
            
        entropies.append(entropy)

    return entropies

def load_fasta(filepath):
    """
    Simple FASTA parser.
    Returns a list of sequence strings.
    """
    sequences = []
    current_seq = []
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_seq:
                    sequences.append("".join(current_seq))
                    current_seq = []
            else:
                current_seq.append(line)
        # Don't forget the last one
        if current_seq:
            sequences.append("".join(current_seq))
            
    return sequences

def main():
    filepath = "/Users/lesz/Documents/academic-integrity-agent/Caste_Study/Entropic_Vise/HIV_Sequence_DB/HIV1_FLT_2022_env_PRO.fasta"
    print(f"Loading sequences from {filepath}...")
    sequences = load_fasta(filepath)
    print(f"Loaded {len(sequences)} sequences.")
    
    if not sequences:
        print("Error: No sequences found.")
        return

    # Verify alignment length consistency (just a quick check)
    first_len = len(sequences[0])
    print(f"Alignment length: {first_len} positions.")
    
    print("Calculating Shannon Entropy per position...")
    entropies = calculate_shannon_entropy(sequences)
    
    # Identify "Entropic Vise" Candidate Zones
    # Threshold: Entropy < 0.1 (Extremely conserved)
    # But ignoring "all-gap" columns (None)
    
    print("\n--- Identifying 'Entropic Vise' Candidates (Entropy < 0.1) ---")
    
    conserved_regions = []
    current_region = []
    
    for i, entropy in enumerate(entropies):
        if entropy is not None and entropy < 0.1:
            if not current_region:
                 current_region = [i + 1] # Start of region (1-indexed for humans)
            # Continue region
        else:
            if current_region:
                # Region ended
                start = current_region[0]
                end = i # Previous position was the end
                length = end - start + 1
                if length >= 5: # Only report regions longer than 5 AA
                     conserved_regions.append((start, end, length))
                current_region = []
                
    # Check if a region was active at the very end
    if current_region:
        start = current_region[0]
        end = len(entropies)
        length = end - start + 1
        if length >= 5:
            conserved_regions.append((start, end, length))

    # Print Results
    print(f"Found {len(conserved_regions)} candidate regions > 5 AA length.\n")
    print(f"{'Start':<10} {'End':<10} {'Length':<10}")
    print("-" * 30)
    for start, end, length in conserved_regions:
        print(f"{start:<10} {end:<10} {length:<10}")

if __name__ == "__main__":
    main()
