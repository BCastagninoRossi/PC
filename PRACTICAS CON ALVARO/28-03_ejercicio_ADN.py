# # -*- coding: utf-8 -*-

# # Nucleotides: 
#     A: Adenine
#     T: Thymine
#     G: Guanine
#     C: Cytosine
    
# 3 billon base pairs in human DNA, they reside in 23 pairs of chromosomes.
# Many parts of the genome have many repetitions of the same nucleotide and are candidate for compression

# Write a function that takes a DNA strand with the read of the sequencer and encodes it replacing repeated 
# nucleotides with the number of repetitions followed by the repeated nucleotide
# for example given the sequence TTTAGGTC the program should output 3TA2GTC:
    
# args: 
#     strand (str): full DNA sequence
    
# returns:
#     strand (str): compressed DNA sequence
    
def compressor (strand: str)->str:
    counter = 1
    for i in range (len(strand)-1):
            if strand[i]==strand[i+1]:
                counter +=1
            elif :
                print(f'{counter}{strand[i]}')
                counter = 1
            else
                
            
        

          
            
