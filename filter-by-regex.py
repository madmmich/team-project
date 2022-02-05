# Initiated by Kelsey Kraus
#
# Contributors: Michael, <UPDATE ME!> 
#
# Description: <UPDATE ME!> This file currently contains the instructions for replicating the data cleaning method implemented by CTK 2016, #ML as well as code that does replicate it.


# NOTE: the suggested approaches below are NOT the only way to complete this task! It is merely given as a starting point. You can choose to do this in a different way if you want, but be sure to comment on your process along the way.

#ML filter-by-regex.py  

# !!! You may need to run in your Shell: pip install pandas !!!



import os
import pandas
import re
import csv

#ML The print(content) command some lines below is unable to print some of the characters from the tweet data from the web here in replit.
#ML This is because, as typing "locale" in the shell shows, replit is set by default to POSIX for encoding, seemingly. Switching it to UFT-8 encoding may be required 


from pandas import * #ML The read_csv() command only works with this line present (though we may not use the csv_read() command), see:  https://www.geeksforgeeks.org/python-read-csv-columns-into-list/   




#ML an alternative attempt at reading the file, didn't fully work:
#allTweets = read_csv("pro-who-tweets.csv")
#fileopen = open('pro-who-tweets.csv')
#allTweets = fileopen.read()


tweets2 = pandas.read_csv('pro-who-tweets.csv', encoding = 'utf-8')
#content = tweets2['content'].toList()
column = tweets2.content
print(f"\nLength of the column for content and current type: \n {len(column)}  {type(column)}")
content = column.tolist() 
#l in tolist() has to be lowercase!!!!!! But why didn't it work in commented out block several lines below?

print(f"\nLength of it converted to list (should be identical) and type for confirmation:\n{len(content)}  {type(content)}")

#ML Former attempt at copying the column:
# content = allTweets[1].tolist()
# print(len(content))


# -- Preprocessing: -- We don't care about the other data in our .csv. We want to only get the tweet text data in 'content' column.
# -- Suggested approach: -- create a list variable and save the 'content' column of the pro-who-tweets.csv file as your list. Print the length of the list. See here for more: https://www.geeksforgeeks.org/python-read-csv-columns-into-list/





# === Part 1: Filtering ===

# -- First filter: -- Remove duplicates. 
# -- Suggested approach: -- using your list, convert the list into a dictionary, which will automatically remove duplicates. Then convert your dictionary back into a list. Print the length of the list. https://www.w3schools.com/python/python_howto_remove_duplicates.asp

content = list(dict.fromkeys(content))
print('Filter 1:',len(content)) 



# -- Second filter: -- Remove tweets where the last non-whitespace character before the word 'who' is not a letter or a comma. See Lecture 3 slides for more explanation of this!
# -- Suggested approach: -- Use the list you created as a result of the previous filter. Save the 10 possible pronouns in a list. Create a loop to run through each entry in your list. Use a conditional statement to construct a regular expression match, and save the list elements matching your condition. Print the length of the list.

pronouns = ["he", "she", "it", "him", "her", "they", "them", "we", "us", "you"]




# pos = []

# for element in content:
#   pos = re.findall("[a-zA-Z]|[\,]\s*\bwho\b", element)
#   if len(pos) > 0:
#     holder.append(element)

# content = holder

# print(len(content))
holder = content
holder2 = []
for element in holder:
  #if bool(re.search("[a-zA-Z|\,]\s*\bwho\b", string)) == True:
  if bool(re.search(r"[,a-zA-Z]\s*\bwho\b", element)) == True:
    holder2.append(element)


print('Filter 2:',len(holder2))

#ML "\s*" in regex means any whitespace character (\s) matched any number of times it appears contiguosly there (*).
#The brackets in [a-zA-z|\,] indicate that it is for one character. The interior text indicates either a letter or a comma.

#1b is a word boundary, means it is next to any non word character(whitespaces, puncutation, etc)


# -- Third filter: -- Remove the pattern 'of PRO who'
# -- Suggested approach: -- Create another loop, and another conditional statement using a regular expression from the list you got from the previous filter. This time, save only those that DO NOT match the conditional statement. Print the length of the list.

holder3 = holder2
holder4 = []
for element in holder3:
  if bool(re.search(r"\bof\b\W*(he|she|it|him|her|they|them|we|us|you|he\,|she\,|it\,|him\,|her\,|they\,|them\,|we\,|us\,|you\,)\s*\bwho\b", element)) == False:
    holder4.append(element)




print('Filter 3:',len(holder4))
#ML The bool() seems to be crucial, this loop didn't work without it.

# -- Fourth filter: -- Remove tweets where the pronoun 'it' preceeds the word 'who' by 2-4 words
# -- Suggested approach: -- Write a regular expression that picks out this pattern. Using the list you generated from the previous filter, use create a loop with a conditional statement that removes this pattern. Print the length of the list.

holder5 = holder4



for element in holder5:
  if bool(re.search(r"(\bit\b)(\s)(.\w[^\s]+){2,4}\s(\bwho\b)", element, re.IGNORECASE)) == True:
    holder5.remove(element)



print('Filter 4:',len(holder5))   
#(\b\b\s*){0|1|2}" should mean a word with any number of whitespaces after 0 or 1 or 2 times.


# -- Fifth filter: -- Remove tweets where 'PRO who' is preceded by the verbs 'ask', 'tell', 'wonder', 'inform', and 'show'.
# -- Suggested approach: --  Save the verbs above into a list. Create a loop that iterates through your pronoun list from above, and removes examples that contain the pattern '[element-from-verb-list] [element-from-PRO-list]'. Print the length of the list.

holder6 = holder5
holder7 = []

for element in holder6:
  if bool(re.search(r"\bask\b|\btell\b|\bwonder\b|\binform\b|\bshow\b\s*(he|she|it|him|her|they|them|we|us|you)\s*\bwho\b", element)) == False:
    holder7.append(element)

print('Filter 5:',len(holder7))



#ML using this link: https://www.geeksforgeeks.org/writing-csv-files-in-python/

#From part2
# The following takes our two lists, tweetList and trueFalseList, and zips them together. It then creates a dataframe out of this list, that can then be converted to a .csv file







# output your list as a .csv or .tsv file.






# === Part 2: Uniqueness ===

# -- Instruction: -- You now need to find out whether the tweets you have left are "literary" or "non-literary", according to CTK's classification. I've written a bit of this for you. Modify the block of code below so that it runs with your variable names. You should replace 'tweetList' in the 'for' block with your variable name that holds the final filtered list of 'PRO who' tweets.

# Test variable: contains a short list of test utterances for the pattern "who <word1> <word2>"
tweetList = ['this is a quote: he who shall not be named', 'who among us really', 'jeff is wondering who sings', 'he who shall not be named again', 'but who among us is perfect']

# This evaluates each tweet in TweetList for whether it contains the specified regex search, and whether that regex pattern in a tweet matches exactly to any other tweet in the list. If it does, it is assigned a value True. If it doesn't, it's assigned a value False.
for tweet in holder7:
  whoPhrase = re.search("who \w+ \w+", tweet)
  try:
    trueFalseList = [whoPhrase.group() in tweet for tweet in holder7]
  except AttributeError:
    trueFalseList = False
print(trueFalseList)

# The following takes our two lists, tweetList and trueFalseList, and zips them together. It then creates a dataframe out of this list, that can then be converted to a .csv file


annotatedTweetList = list(zip(holder7, trueFalseList))
tweetDataframe = pandas.DataFrame(annotatedTweetList)
tweetDataframe.to_csv('literary-annotated-tweets.csv', header=["Tweet-text", "Uniqueness"], index=False)
