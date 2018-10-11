name = input("What is your name? : ")

age = input("What is your age? ")
if age <= 18:
    print("Under 18")
elif age >= 18 and age <= 25:
    print("Between 18 and 25")
elif age >= 25:
    print("Over 25")
"""Say if you are a)Under 18. b)Between 18 and 25. c)Over 25. : """

height = input("How tall are you? ")
"""Say if you are a)Under 160cm. b)Between 160cm and 180cm. c)Over 180cm : """

weight = input("How much do you weight? ")
"""Say if you are a)Under 60kg. b)Between 60kg and 80kg. c)Over 80kg : """

eye = input("What is the color of your eyes? : ")

hair = input("What is the color of your hair? : ")

print(f"Hello, my name is {name}, I'm {age} years old. "
      f"I'm about {height} centimetres tall and I weight {weight} kilos. "
      f"Oh also, I have {eye} eyes and {hair} hair.")
