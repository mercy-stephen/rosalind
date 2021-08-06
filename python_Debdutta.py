#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = "Name: Debdutta Chatterjee"
print (n)

e = "Email: debduttachatterjee00@gmail.com"
print (e)

u = "<Slack Username>: @dev00001122"
print (u)

b = "Biostacks: Genomics, Transcriptomics, Vaccine Informics, Public Health and Genomic Epidemiology"
print (b)

t = "<Twitter Handle>: @dev00001122"
print (t)


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

print("<Hamming distance>:",(hammingDist(AB, CD)))


# In[ ]:




