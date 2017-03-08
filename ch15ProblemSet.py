#graded
'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

dictionary = open("dictionary.txt", "r")
word_length = 0
longest_word = ''

for word in dictionary:
    if len(word)-1 > word_length:
        word_length = len(word)-1
        longest_word = word
    if len(word)-1 == word_length:
        longest_word = word



print(word_length)
print(longest_word)




#2.  (10pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"


import re
def split_line(line):
    # This function takes in a line of text and returns a list of words in the line
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file1 = open("AliceInWonderLand.txt", "r")

total = []
letters = 0

for line in file1:
    word = split_line(line)
    for i in range(len(word)):
        total.append(word[i])
    for j in range(len(word)):
        letters += len(word[j])

print('There are', len(total), 'words found in the text.')
average = letters / len(total)
print(average)



# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

cat_total = 0
cheshire_total = 0
cheshire_cat_total = 0

for i in range(len(total)):
    if total[i].lower() == 'cat':
        cat_total += 1
    if total[i].lower() == 'cheshire':
        cheshire_total += 1
    if total[i].lower() == 'cheshire' and i < (len(total)-1):
        if total[i + 1].lower() == 'cat':
            cheshire_cat_total += 1

print(cat_total)
print(cheshire_total)
print(cheshire_cat_total)





#### OR #####

#3  (13pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"


# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



