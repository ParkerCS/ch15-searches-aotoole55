'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

file = open("dictionary.txt", "r")

dictionary_list = []

for line in file:
    for words in line:
        dictionary_list.append(words)
file.close()

print(dictionary_list)

print('---Linear Search---')
alice_file = open("AliceInWonderLand200.txt", "r")
line_number = 0

for line in alice_file:
    words = split_line(line)
    line_number += 1
    for i in range(len(words)):
        for j in range(len(dictionary_list)):
            if words[i].lower() == dictionary_list[j].lower():
                break
            elif j == len(dictionary_list):
                print(words[i],'on line', line_number, 'was not found.')

alice_file.close()


print('---Binary Search---')


alice_file = open("AliceInWonderLand200.txt", "r")
line_number = 0

lower_bound = 0
upper_bound = len(dictionary_list)-1

found = False




for line in alice_file:
    words = split_line(line)
    line_number += 1
    for i in range(len(words)):
        while lower_bound <= upper_bound and not found:
            middle_position = (lower_bound + upper_bound) // 2
            if dictionary_list[middle_position].lower() < words[i].lower():
                lower_bound += middle_position + 1
            elif dictionary_list[middle_position].lower() > words[i].lower():
                upper_bound -= middle_position - 1
            else:
                found = True
        if not found:
            print(words[i],'on line', line_number, 'was not found.')

alice_file.close()
