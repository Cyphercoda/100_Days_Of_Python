# Tickiting system in a park

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height <= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age > 18:
        print("pay $17")
    elif age < 12:
        print("pay $5")
    elif age > 12 < 18:
        print("pay $12")
else:
    print("sorry, you have to grow taller before you can ride")
