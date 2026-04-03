# Map DNA sequences to digital structures

def map_dna_to_digital(dna_sequence):
    """
    Maps a DNA sequence to a digital representation.
    For simplicity, this example maps DNA to binary (A -> 00, T -> 01, C -> 10, G -> 11).

    Args:
    - dna_sequence (str): A string representing the DNA sequence (e.g., "ATCG").

    Returns:
    - digital_representation (str): A binary string representing the digital form of the DNA.
    """
    mapping = {'A': '00', 'T': '01', 'C': '10', 'G': '11'}
    digital_representation = ''.join(mapping[nucleotide] for nucleotide in dna_sequence)
    return digital_representation

if __name__ == "__main__":
    # Example mapping
    dna_sequence = "ATCG"
    digital_rep = map_dna_to_digital(dna_sequence)
    print(f"Digital Representation: {digital_rep}")
