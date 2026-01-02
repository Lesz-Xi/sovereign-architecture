from entropy_calculator import load_fasta

def map_alignment_to_hxb2(filepath, regions_of_interest):
    """
    Maps alignment indices to HXB2 numbering.
    HXB2 is assumed to be the first sequence in the file (Standard Los Alamos format).
    """
    sequences = load_fasta(filepath)
    if not sequences:
        print("Error: No sequences loaded.")
        return

    # 1. Get HXB2 Reference Sequence
    hxb2_seq = sequences[0]
    # Header was >B.FR.83.HXB2... so this is correct.
    
    print(f"Reference Length (Alignment): {len(hxb2_seq)}")
    
    # 2. Build Mapping
    # alignment_index (0-based) -> (AminoAcid, HXB2_Number)
    align_map = {}
    hxb2_counter = 0
    
    for i, char in enumerate(hxb2_seq):
        if char not in ['-', '?', '.']:
            hxb2_counter += 1
            align_map[i] = (char, hxb2_counter)
        else:
            align_map[i] = (char, None) # Gap in HXB2

    # 3. Analyze Regions
    print("\n--- Mapping 'Entropic Vise' Regions to HXB2 ---\n")
    print(f"{'Align Start':<12} {'Align End':<10} {'HXB2 Start':<12} {'HXB2 End':<10} {'Sequence Fragment':<25}")
    print("-" * 75)

    for start_align, end_align in regions_of_interest:
        # Convert 1-based (report) to 0-based (python index)
        # Sequence: 1231-1250 -> Index: 1230-1249
        idx_start = start_align - 1
        idx_end = end_align - 1 
        
        # Get HXB2 coords
        start_residue = align_map.get(idx_start, ('?', None))
        end_residue = align_map.get(idx_end, ('?', None))
        
        # Extract the sequence fragment from HXB2
        # Note: We need to handle gaps inside the fragment if they exist in HXB2 
        # (though they shouldn't in a reference usually, unless inserted against itself?)
        fragment = hxb2_seq[idx_start : idx_end+1].replace('-', '')
        
        # Format output
        hxb2_s_str = f"{start_residue[0]}{start_residue[1]}" if start_residue[1] else "Gap"
        hxb2_e_str = f"{end_residue[0]}{end_residue[1]}" if end_residue[1] else "Gap"
        
        print(f"{start_align:<12} {end_align:<10} {hxb2_s_str:<12} {hxb2_e_str:<10} {fragment:<25}")

def main():
    filepath = "/Users/lesz/Documents/academic-integrity-agent/Caste_Study/Entropic_Vise/HIV_Sequence_DB/HIV1_FLT_2022_env_PRO.fasta"
    
    # Regions from the Corrected Entropy Analysis (>50% Occupancy)
    regions = [
        (1358, 1366), # Primary Target (9 AA)
        (1328, 1333),
        (587, 591),
        (177, 181),
        (1552, 1556)
    ]
    
    map_alignment_to_hxb2(filepath, regions)

if __name__ == "__main__":
    main()
