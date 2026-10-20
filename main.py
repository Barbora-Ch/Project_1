# %%
# výchozí texty k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# %%
# registrovaní uživatelé
users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"   
}

# %%
# přihlášení uživatele
username = input("username: ")
password = input("password: ")

if username in users and users[username] == password:
    print("-" * 40)
    print("Welcome to the app, " + username)
    text_count = len(TEXTS)
    print("We have " + str(text_count) + " texts to be analyzed.")
    print("-" * 40)
# volba textu
    select = input("Enter a number btw. 1 and " + str(text_count) + " to select: ")
    if select.isdigit() and int(select) >= 1 and int(select) <= text_count:
        selected_text = TEXTS[int(select) - 1]
        print("-" * 40)
    else:
        print("Invalid selection. Please enter a number between 1 and " + str(text_count) + ".")
        quit()
else: 
    print("unregistered user, terminating the program..")
    quit()
    

# %%
# analýza textu

# rozděl text na slova
words = selected_text.split()
print("There are " + str(len(words)) + " words in the selected text.")

# spočítej titlecase words (všechna slova, která začínají velkým písmenem)
titlecase_words = 0
for word in words:
    if word.istitle():
        titlecase_words += 1
print("There are " + str(titlecase_words) + " titlecase words.")

# spočítej uppercase words (všechna slova, která jsou psána velkými písmeny)
uppercase_words = 0
for word in words:
    if word.isupper():
        uppercase_words += 1
print("There are " + str(uppercase_words) + " uppercase words.")

# lowercase words (všechna slova, která jsou psána malými písmeny)
lowercase_words = 0
for word in words:
    if word.islower():
        lowercase_words +=1
print("There are " + str(lowercase_words) + " lowercase words.")

# numeric strings
numeric_strings = 0
for word in words:
    if word.isnumeric():
        numeric_strings += 1
print("There are " + str(numeric_strings) + " numeric strings.")

# sum of all the numbers in the text
numeric_sum = 0
for word in words:
    if word.isnumeric():
        numeric_sum += int(word)
print("The sum of all numbers in the text is: " + str(numeric_sum))
print("-" * 40)

# bar chart of word lengths 
lengths = {}
for word in words:
    length = len(word)
    if length in lengths:
        lengths[length] += 1
    else:
        lengths[length] = 1
print("LEN|   " + "OCCURRENCES        " + "|NR.")
print("-" * 40)

for length in sorted(lengths):
    print(str(length).ljust(3) + "| " + ("*" * lengths[length]).ljust(20) + " |" + str(lengths[length]))