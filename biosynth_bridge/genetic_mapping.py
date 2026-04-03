from biosynth_bridge.genetic_mapping import map_dna_to_digital

# Example DNA sequence
dna_sequence = "ATCGTACGAGT"

# Map the DNA to a digital structure (represented as binary here)
digital_rep = map_dna_to_digital(dna_sequence)
print(f"Digital Representation: {digital_rep}")
