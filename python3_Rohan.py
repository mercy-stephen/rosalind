 # HackBio Internship 2021 
name= ("Name:Rohan Kumar")
print (name)

email = ("Email:rohancoolraj5@gmail.com")
print (email)

username = ("<Slack_Username>:@Rohanraj11")
print (username)

Twitter = ("<Twitter_username>:@Rohan11322")
print (Twitter)

Biostacks = ("Biostack:Genomics")
print (Biostacks)

def hammingDistance(slack, twitter):
    i = 0
    count = 0
 
    while(i < len(slack)):
        if(slack[i] != twitter[i]):
            count += 1
        i += 1
    return count
 

slack = "Rohanraj11"
twitter = "Rohan11322"
 
print(f"<Hamming distance>:{hammingDistance(slack, twitter)}")
