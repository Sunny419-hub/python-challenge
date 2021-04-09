# Import the necessary dependencies
import os
import csv
import re
from statistics import mean

# Read in a .csv file
csv_file = os.path.join("C:\\Users\\ssses\\Desktop\\python-ch\\python-challenge\\PyParagraph\\Resources", "paragraph_1.txt")

with open(csv_file, 'r') as txtfile:
  lines = txtfile.read()

#Approximate Word Count
word_list = lines.split()
word_count = len(word_list)

#Approximate Sentence Count
sentence_list = lines.split('.')
sentence_count = len(sentence_list)

#Average Letter Count
letter_count = 0

for word in word_list :
    letter_count += len(word)
    average_letter_count = '{0:.1f}'.format(letter_count/word_count)

#Average Sentence Length
sentences = re.split("(?<=[.!?]) +", lines)
words_in_sentence = []

for sentence in sentences :
    words_in_sentence.append(len(sentence.split()))

#Terminal results
print(f'Paragraph Analysis')
print(f'-----------------')
print(f'Approximate Word Count: {word_count}')
print(f'Approximate Sentence Count: {sentence_count}')
print(f'Average Letter Count: {average_letter_count}')
print(f'Average Sentence Length: {(mean(words_in_sentence))}')


# Specify the file to write to
output_path = os.path.join("c:\\Users\\ssses\\Desktop\\python-ch\\python-challenge\\PyPoll\\analysis","new.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:
  txtwriter = csv.writer(txtfile, delimiter=',')
  txtwriter.writerow([f'Paragraph Analysis'])
  txtwriter.writerow([f'-------------------------'])
  txtwriter.writerow([f'Approximate Word Count: {word_count}'])
  txtwriter.writerow([f'Approximate Sentence Count: {sentence_count}'])
  txtwriter.writerow([f'Average Letter Count: {average_letter_count}'])
  txtwriter.writerow([f'Average Sentence Length: {(mean(words_in_sentence))}'])