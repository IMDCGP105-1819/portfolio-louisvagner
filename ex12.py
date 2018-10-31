def hotelCost(): 
    days = raw_input ("How many nights will you stay at the hotel?")
    total = 140 * int(days)
    print ("The total cost is",total,"dollars")
    return total


def planeRideCost(): 
    city = raw_input ("Wich city will you travel to\n")
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475
    else:
        print ("That's not a valid destination")

def rentalCarCost(): 
    rental_days = raw_input ("How many days will you rent the car\n")   
    discount_3 = 40 * int(rental_days) * 0.2 
    discount_7 = 40 * int(rental_days) * 0.5 
    total_rent3 = 40 * int(rental_days) - discount_3
    total_rent7 = 40 * int(rental_days) - discount_7
    cost_day = 40 * int(rental_days) 

    if int(rental_days) >= 3: 
        print ("The total cost is", total_rent3, "dollars")
        return total_rent3
    elif int(rental_days) >= 7: 
        print ("The total cost is", total_rent7, "dollars")
        return total_rent7
    else: 
        print( "The total cost is", cost_day, "dollars")
        return cost_day

def tripCost():
    travel_city = raw_input ("What's our destination\n")
    days_travel = raw_input ("\nHow many days will you stay\n")
    total_trip_cost = hotelCost(int(day_travel)) + planeRideCost () + rentalCarCost(int(days_travel))
    return "The total cost with the trip is", total_trip_cost

tripCost()
