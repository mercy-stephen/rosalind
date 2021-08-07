#!/usr/bin/env python
# coding: utf-8


n = "Name:Dibyendu Biswas"
print (n)

e = "Email:biswasdibyendu39@gmail.com"
print (e)

u = "<Slack_Username>:@Dibyendu1153533"
print (u)

t = "<Twitter_Handle>:@Dibyend11153533"
print (t)

b = "Biostack:Genomics & Transcriptomics"
print (b)

def hammingDist(SU, TH):
    i = 0
    count = 0
 
    while(i < len(SU)):
        if(SU[i] != TH[i]):
            count += 1
        i += 1
    return count

 
SU = "Dibyendu1153533"
TH = "Dibyend11153533"
print(f"<Hamming_Distance>:{(hammingDist(SU, TH))}")


