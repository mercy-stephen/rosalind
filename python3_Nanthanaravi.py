#!usr/bin/python

print("Name:Nanthana Ravichandran")
print("Email:nanthanaravichandran@gmail.com")
print("<Slack_username>:@Nanthanaravi")
print("<Twitter_username>:@nanthanaravi")
print("Biostack:Transcriptomics")

slack_username = "@Nanthanaravi"
twitter_username = "@nanthanaravi"

def hammingDist(slack_username, twitter_username):
    i = 0
    count = 0
    while(i < len(slack_username)):
        if(slack_username[i] != twitter_username[i]):
            count += 1
        i += 1
    return count
print(f"<Hamming distance>:{hammingDist(slack_username, twitter_username)}")
