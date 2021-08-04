 # HackBio Internship 2021 
print("Name: Aditi Singh")
print("Email: singhaditi7733@gmail.com")
print("Slack Username: @AditiSingh12345")

print = ("Twitter username: @@AditiSi28068977")

print("Biostacks: Genomics")


def hammingDistance(slack, twitter):
    i = 0
    count = 0
 
    while(i < len(slack)):
        if(slack[i] != twitter[i]):
            count += 1
        i += 1
    return count
 

slack = "AditiSingh12345"
twitter = "AditiSi28068977"
 
print(hammingDistance(slack, twitter))
