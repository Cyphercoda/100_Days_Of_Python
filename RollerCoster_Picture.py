# Tickiting system in a park

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age > 18:
        bill = 17
        print("pay $17")
    elif age < 12:
        bill = 5
        print("pay $5")
    elif age > 12 < 18:
        bill = 12
        print("pay $12")

    want_photo = input("Do you want a photo? Y or N.")
    if want_photo == "Y":
        bill += 3
        print(f"your bill is: {bill}")
else:
    print("sorry, you have to grow taller before you can ride")
