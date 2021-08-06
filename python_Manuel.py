name ='Emmanuel Ani'
email = 'emmanuelani234@gmail.com'
slack_username = '@emmanuelani234'
biostack = 'Data Science'
twitter_handle ='@emmanuelani234'

def HammingDist(string1, string2):
    i = 0
    count = 0
    while (i<len(string1)):
        if (string1[i] != string2[i]):
            count +=1
        i +=1
    return count


print('Name:', name)
print('Email:', email)
print('Slack_username:', slack_username)
print('Biostack:', biostack)
print('Twitter_handle:', twitter_handle)

a = HammingDist(slack_username, twitter_handle)
print('Hamming_Distance:', a)



