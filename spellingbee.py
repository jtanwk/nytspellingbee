# Spelling Bee Solver

# word source: MIT 10K Word List http://www.mit.edu/~ecprice/wordlist.10000
# longer word source: https://github.com/dwyl/english-words

# initial variables
todays_letters = set(input('Enter today\'s letters:').strip(' ').lower())
required = input('What is the required letter? ').strip(' ').lower()

# import wordlist
word_file = 'data/words.txt'
wordlist = open(word_file).read().split('\n')

# initialize empty answer list
pangrams = []
answers = []

# loop over wordlist and append possible answers
for word in wordlist:

    word = word.lower()

    if len(word) < 4:
        continue
    elif word.find(required) == -1:
        continue
    elif set(word) == todays_letters:
        answers.append(word)
        pangrams.append(word)
    elif set(word) < todays_letters:
        answers.append(word)
    else:
        continue

# organize answers by letter count
answers_4 = []
answers_5 = []
answers_6 = []
answers_7plus = []

for answer in answers:
    if len(answer) == 4:
        answers_4.append(answer)
    elif len(answer) == 5:
        answers_5.append(answer)
    elif len(answer) == 6:
        answers_6.append(answer)
    else:
        answers_7plus.append(answer)

# print answers
print(f"{len(answers)} POTENTIAL ANSWERS FOUND!", '\n-----')
print("Pangrams:", pangrams, '\n-----')
print("4 letters:", answers_4, '\n-----')
print("5 letters:", answers_5, '\n-----')
print("6 letters:", answers_6, '\n-----')
print("7+ letters:", answers_7plus)
