#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
input("Welcome to the TIP Calculator")
Bill = float(input("How much is the total bill?"))
num_of_ppl = int(input("How many person should pay?"))
Tip = int(input("What percentage tip would you like to give? 10 , 12 , 15?"))
Tip_val = Tip / 100
result = (Bill / num_of_ppl) * Tip_val

print(f"Each person should pay: {result}")
