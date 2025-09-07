# Python weight convertor

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()
print(f"You chose {unit}")

if unit == "K":
    weight *= 2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight,1)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight,1)} {unit}")
else: 
    print(f"{unit} was in not valid")

