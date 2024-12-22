#STRING AND NUMBER COMBO SETS
combo1 = {12, 21, 26, 31, 15, "Agatha", "Laura", "Steven", "Rudhvik", "Delilah"}
combo2 = {"Bob", "Agatha", "James", "John", 12, 41, 31, 16, 46}

#printing the sets
print(combo1)
print(combo2)

#uninon and intersection
print(combo1|combo2)
print(combo1&combo2)

#differnce
print(combo1-combo2)
print(combo2-combo1)

#symmetric differnce
print(combo1^combo2)

#PASSWORD GENERATOR
import random, string

def generatePassword():
    characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')  
    passwordLength = random.randint(5, 10)
    password = [] 
    for i in range(passwordLength):
        password.append(random.choice(characters)) 
    return ''.join(password) 
print("Your selected password is:", generatePassword())