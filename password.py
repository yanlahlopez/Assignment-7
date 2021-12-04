password = input("Enter password: ")

Uppercase = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
Lowercase = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
Numbers = ("0","1","2","3","4","5","6","7","8","9")
Special = ("`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|",";",":","'","<",">",",",".","?","/")

lowercase = False
uppercase = False
numbers = False
special = False

for character in password:
    if character in Uppercase:
        uppercase = True
    elif character in password:
        if character in Lowercase:
            lowercase = True

for character in password:
    if character in Numbers:
        numbers = True
    elif character in password:
        if character in Special:
            special = True

if uppercase == False:
    print("Password must contain at least one uppercase letter.")
elif lowercase == False:
     print("Password must contain at least one lowercase letter.")
elif numbers == False:
    print("Password must contain at least one number.")
elif special == False:
    print("Password must contain at least one special character.")
elif len(password) < 15:
    print("Password must contain at least 15 characters.")
else:
    print("Password met all criteria!")