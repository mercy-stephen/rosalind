# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11IOw93xd_uwLNxNHiWXoaqYEPlCITMU9
"""

#!usr/bin/python

name = ("Name:Mohamed Salem")
print (name)

email = ("Email:drmohamedsalem340@gmail.com")
print (email)

username = ("<Slack_Username>:@Salem")
print (username)

Twitter = ("<Twitter_handle>:@drmohamedsalem4")
print (Twitter)

Biostacks = ("Biostacks:Medicinal chemistry and CheminformaticS")
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

print("<Hamming distance>:",(hammingDist(slack, twitter)))
