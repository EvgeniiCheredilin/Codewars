def dna_strand(dna):
    """Takes string of DNA
    Returns complementary side string."""
    my_dna = ""
    for i in dna:
        if i == "A":
            my_dna = my_dna + "T"
        if i == "T":
            my_dna = my_dna + "A"
        if i == "C":
            my_dna = my_dna + "G"
        if i == "G":
            my_dna = my_dna + "C"
    return my_dna
