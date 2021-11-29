import random

score = 0

print("There will be 10 questions for you to answer. Your score will be given at the end of the quiz.")

for i in range(10):
    num1 = random.randrange(0, 99)
    num2 = random.randrange(0, 99)

    print('Add: %s + %s' % (num1, num2))
    answer = num1 + num2

    student = int(input("= "))
    
    if student == answer:
         print("Correct!")
         score += 1
    elif student != answer:
        print("Incorrect.")

print(f"Total score: {score}/10")

if score > 7:
    print("Well done! Keep it up.")
else:
    print("Try again next time!")