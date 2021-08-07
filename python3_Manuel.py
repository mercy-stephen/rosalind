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


print(f'Name:{name}')
print(f'Email:{email}')
print(f'<Slack_username>:{slack_username}')
print(f'<Twitter_handle>:{twitter_handle}')
print(f'Biostack:{biostack}')

a = HammingDist(slack_username, twitter_handle)
print(f'<Hamming_Distance>:{a}')



