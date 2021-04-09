# Import the necessary dependencies
import os
import csv
import re
from statistics import mean
# Read in a .csv file
csv_file = os.path.join("C:\\Users\\ssses\\Desktop\\python-ch\\python-challenge\\PyParagraph\\Resources", "paragraph_1.txt")

with open(csv_file, 'r') as txtfile:
  lines = txtfile.read()


print(f'Paragraph Analysis')
print(f'-----------------')

#Approximate Word Count
word_list = lines.split()
word_count = len(word_list)
print(f'Approximate Word Count: {word_count}')

#Approximate Sentence Count
sentence_list = lines.split('.')
sentence_count = len(sentence_list)
print(f'Approximate Sentence Count: {sentence_count}')

#Average Letter Count
letter_count = 0

for word in word_list :
    letter_count += len(word)
    average_letter_count = '{0:.1f}'.format(letter_count/word_count)

print(f'Average Letter Count: {average_letter_count}')

#Average Sentence Length

sentences = re.split("(?<=[.!?]) +", lines)
words_in_sentence = []

for sentence in sentences :
    words_in_sentence.append(len(sentence.split()))
    
print(f'Average Sentence Length: {(mean(words_in_sentence))}')




with open(output_file, 'r') as txtfile:
        lines = txtfile.read()
        print(lines)

