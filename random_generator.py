import random
# random module imported

wordlist = [] # empty list
symbols = ['#', '&', '@', '!', '$']  # special characters used

with open("documentation-text.txt", 'r') as file:
    data = file.readlines()

    # using for loop to iterate
    for line in data:
        words = line.split()

        for item in words:
            if len(item) > 5:
                wordlist.append(item.capitalize())

word = random.choice(wordlist)      # used random.choice function
s_char = random.choice(symbols)
digits = str(random.randint(20,199))  # used random.randint function

# combining three variables to generate 
# random readable password
combine = word + s_char + digits
print(combine)