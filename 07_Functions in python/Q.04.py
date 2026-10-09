# WAP to comvert USD to INR
inr = float(input("Enter the amount : "))

# Function for converting USD to INR...............
def USD_to_INR(inr):
    USD_rate = inr * 92
    print(f"{inr} USD = {USD_rate} inr")

USD_to_INR(inr)