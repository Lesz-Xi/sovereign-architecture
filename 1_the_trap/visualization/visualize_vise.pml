# PyMOL Script for "The Entropic Vise" Visualization
# Target Structure: PDB 5FUU (HIV-1 BG505 SOSIP.664 Trimer)
# Usage: Run in PyMOL via "File > Run" or command "pymol visualize_vise.pml"

# 1. Load the Structure
fetch 5fuu, async=0

# 2. Clean Up View
hide all
bg_color white
select protein, polymer.protein
show cartoon, protein
color gray80, protein

# 3. Highlight "The Entropic Vise" Targets (HXB2 Coordinates)

# TARGET 1: HR1 "The Spring" (Residues 568-576)
# Significance: Primary Target. Immutability Index: Rank 1.
select vise_hr1, resi 568-576
color red, vise_hr1
show spheres, vise_hr1
label first vise_hr1, "HR1 Vise"

# TARGET 2: MPER "The Anchor" (Residues 678-682)
# Significance: bNAb Supersite. Immutability Index: Rank 2.
select vise_mper, resi 678-682
color orange, vise_mper
show spheres, vise_mper
label first vise_mper, "MPER Vise"

# TARGET 3: N-HR1 (Residues 547-552)
select vise_nhr1, resi 547-552
color salmon, vise_nhr1

# TARGET 4: C2 Domain (Residues 247-251)
select vise_c2, resi 247-251
color yellow, vise_c2

# TARGET 5: C1 Domain (Residues 52-56)
select vise_c1, resi 52-56
color lightblue, vise_c1

# 4. Final Polish
deselect
zoom
set sphere_scale, 1.2
set transparency, 0.4
create vise_surface, vise_hr1 or vise_mper
show surface, vise_surface

print "Entropic Vise Visualization Loaded."
print "Red = HR1 (Primary Target)"
print "Orange = MPER"
