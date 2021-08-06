Data={"Name:":"Eslam Mohammed Shedid", "Email:":"Eslamshedid55520@gmail.com" , "<Slack_username>:":"@Eslam55520" , "Biostack:":"Genomics" , "twitter_handle:":"@Eslam15112"  }
counter=0
for a in Data:
    print a + Data[a]
s1=Data["<slack_username:>"]
s2=Data["<twitter_handle:>"]
for x in range(len(s1)):
    if s1[x]!=s2[x]:
        counter+=1
print "Hamming_Distance:" +`counter` 
x=input("if you want to end the program press enter")
