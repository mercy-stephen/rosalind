#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = "Name: Dibyendu Biswas"
print (n)

e = "Email: biswasdibyendu39@gmail.com"
print (e)

u = "<Slack Username>: @Dibyendu1153533"
print (u)

b = "Biostacks: Genomics, Transcriptomics, Data Science, Vaccine Informics, Public Health and Genomic Epidemiology"
print (b)

t = "<Twitter Handle>: @Dibyend11153533"
print (t)


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

print("<Hamming distance>:",(hammingDist(SU, TH)))


# In[ ]:



