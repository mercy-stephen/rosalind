name ='Emmanuel Ani'
email = 'emmanuelani234@gmail.com'
slack_username = '@Manuel'
biostack = 'Data Science'
twitter_handle ='emmanuelani234'

def hammingDistance(string1, string2):
    i = 0
    count = 0
        while i < len(string1):
            if (string1[i] != string2[i]):
                count += 1
            i += 1
        return count

print(name)
print(email) 
print(slack_username)
print(biostack)
print(twitter_handle)

hammingDistance(slack, twitter_handle)
