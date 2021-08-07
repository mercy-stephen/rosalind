#!usr/bin/python
# -*- coding: utf-8 -*-

name = ("Name:Mohamed Salem")
print (name)

email = ("Email:drmohamedsalem340@gmail.com")
print (email)

username = ("<Slack_Username>:@Salem")
print (username)

Twitter = ("<Twitter_handle>:@drmohamedsalem4")
print (Twitter)

Biostacks = ("Biostack:Medicinal chemistry and CheminformaticS")
print (Biostacks)


def hammingDist(slack, twitter):
    i = 0
    count = 0
 
    while(i < len(slack)):
        if(slack[i] != twitter[i]):
            count += 1
        i += 1
    return count

 
slack = "Salem"
twitter = "drmohamedsalem4"

print(f"<Hamming distance>:{(hammingDist(slack, twitter))}")
