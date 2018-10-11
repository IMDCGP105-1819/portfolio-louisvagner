name = input("What is your name? : ")

age = input("What is your age? : ")
if age <= "17":
    print("--> Under 18")
elif age >= "18" and age <= "21":
    print("--> Between 18 and 21")
elif age >= "22":
    print("--> Over 21")

height = input("How tall are you? (in cm) : ")
if height <= "160":
    print("--> Under 160 centimetre")
elif height >= "160" and height <= "180":
    print("--> Between 160 and 180 centimetre")
elif height >= "180":
    print("--> Over 180 centimetre")

weight = input("How much do you weight? : ")
if weight <= "60":
    print("--> Under 60 kilos")
elif weight >= "60" and weight <= "80":
    print("--> Between 60 and 80 kilos")
elif height >= "80":
    print("--> Over 80 kilos")

eye = input("What is the color of your eyes? : ")

hair = input("What is the color of your hair? : ")

print(f"Hello, my name is {name}, I'm {age} years old. "
      f"I'm about {height} centimetres tall and I weight {weight} kilos. "
      f"Oh also, I have {eye} eyes and {hair} hair.")
