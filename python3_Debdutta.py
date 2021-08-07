#!/usr/bin/env python
# coding: utf-8


n = "Name:Debdutta Chatterjee"
print (n)

e = "Email:debduttachatterjee00@gmail.com"
print (e)

u = "<Slack_Username>:@dev00001122"
print (u)

t = "<Twitter_handle>:@dev00001122"
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

 
AB = "dev00001122"
CD = "dev00001122"

print(f"<Hamming_Distance>:{(hammingDist(AB, CD))}")




