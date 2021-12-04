sentence = input("Provide your statement: ")

Vowels = 0
Consonants = 0

words = sentence.split()
countwords = len(words)

print("Number of Words: ", countwords, sep=" ")

vowels = ["A","E","I","O","U","a","e","i","o","u"]
for char in sentence:
    if char in vowels:
        Vowels = Vowels+1

print("Number of Vowels: ", Vowels)

consonants = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z","b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
for char in sentence:
    if char in consonants:
        Consonants = Consonants+1

print("Number of Consonants: ", Consonants)