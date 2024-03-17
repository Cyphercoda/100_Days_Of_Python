
bill = float (input ("what is your total bill ?"))
tip_percentage= (float (input ("tip percentage?")))/100
total_tip = bill * tip_percentage
Number_of_people=int(input("Number of people ?"))
total_bill = bill + total_tip
split = round((total_bill / Number_of_people), 2)
print(f"Each person will pay {split}")
