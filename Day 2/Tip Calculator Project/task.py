print("Welcome to the tip calculator!")


bill = float(input("What was the total bill? €"))
tip = int(input("What percentage tip would you like to give? 10 12 15 (do not add % sign)"))
people = int(input("How many people to split the bill? "))


total_pay= round(bill*(1+tip/100))
print(f"Total bill included tips is {total_pay}")

total_pay_per_person= total_pay // people
print(f"Each person pays: €{total_pay_per_person}")

#comment on my code: you need to break it down more, this is too short-cut
#anything unclear - print it out after every step!