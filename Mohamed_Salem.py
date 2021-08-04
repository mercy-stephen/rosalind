#!usr/bin/python

name = ("Name: Mohamed Salem")
print (name)

email = ("email: drmohamedsalem340@gmail.com")
print (email)

username = ("Slack Username: @Salem")
print (username)

Twitter = ("Twitter username: @drmohamedsalem4")
print (Twitter)

Biostacks = ("Biostacks: Medicinal chemistry and CheminformaticS")
print (Biostacks)


def hammingDist(slack_username, twitter):
    i = 0
    count = 0
 
    while(i < len(slack_username)):
        if(slack_username[i] != twitter[i]):
            count += 1
        i += 1
    return count

 
slack_username = "Salem"
twitter = "drmohamedsalem4"

print("<Hamming distance>:",(hammingDist(slack_username, twitter)))
