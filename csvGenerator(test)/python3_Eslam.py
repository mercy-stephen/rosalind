Data={"Name:" :"Eslam Mohammed Shedid", 
      "Email:":"Eslamshedid55520@gmail.com", 
      "slack:":"@Eslam55520",
      "twitter:" : "@Eslam15112",
      "biostack:": "Genomics"
      }

counter=0

for a in Data:
    print(a + Data[a])

s1=Data["slack:"]
s2=Data["twitter:"]

for x in range(len(s1)):
    if s1[x]!=s2[x]:
        counter+=1

print("H_distance:" + str(counter))
