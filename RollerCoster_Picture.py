# Tickiting system in a park

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age <= 12:                                #18:
        bill = 5                                 #17
        print("pay $5")
    elif 18 < age < 45:
        bill = 15
        print("pay $15")
    elif age > 12 and age < 18:           # 12 > age < 18:
        bill = 12
        print("pay $12")
    elif age > 45 and age < 55:          ###45 > age < 55:
        bill = 0
        print("pay $0")

    want_photo = input("Do you want a photo? Y or N.")
    if want_photo == "Y":
        bill += 3
else:
    print("sorry, you have to grow taller before you can ride")

print(f"your bill is: {bill}")