#!usr/bin/julia

########### HACKBIO 2021 ###########
# Stage 0 - Introduction

name = "David Guevara-Apaza"
email = "davidguevaraapaza@gmail.com"
slack = "@yoodavoo"
twitter = "@yooodavo"
biostack = "Data Science & Genomics"

# Julia calculate Hamming distance in 2 (same length) strings

function hammingDist(str1, str2)
    i = 1
    count = 0
    while i < length(str1)
        # print("imprimiendo: ", i)
        if str1[i] != str2[i]
            count += 1
        end
        i += 1
    end
    return count
end
  
##############################
# Stage 0_prints
println("Name:", name)
println("Email:", email)
println("<Slack_username>:", slack)
println("<Twitter_handle>:", twitter)
println("Biostack:", biostack)
# Stage1_print get the hamming distance from the strings
println("<Hammming_Distance>:", hammingDist(twitter, slack))


