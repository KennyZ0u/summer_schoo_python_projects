month = int(input("This program will write a letter to a friend of yours!\nLet's start with the date. what is the month? (please enter a value from 1-12): "))
day = int(input("Great! What is the day? (please enter a value from 1-31): "))
year = int(input("Finaly, what year is it? "))
name_friend = input("Great! what is your friend's name? ")
name_self = input("What is your name? ")
info = input("What would you like to tell your friend? ")
space = " "
print(f"Here is a draft of youur letter to your friend: \n{space:>50} {month:0=2}/{day:0=2}/{year}\nDear {name_friend},\n\t{info}\nSigned!\n{name_self}")