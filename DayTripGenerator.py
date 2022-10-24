# Main Stories
 
# (5 points): As a developer, I want to make at least three commits with descriptive messages 
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation,
#  and entertainment in their own separate Lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, 
# and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10  points): As a user, I want to display my completed trip in the console
# (5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. 
# Remember, each function should do just one thing! 

import random
from tkinter import Y
from urllib import response
#Lists
destinations = ["Los Angeles", "Portland", "Albuquerque", "Dallas", "New Orleans"]
restaurants = ["BBQ", "Japanese", "Thai", "Mexican", "Italian"]
mode_transpo = ["Flight", "Train", "Chauffeur", "Party Bus", "Uber Black"]
entertainmaent = ["Wine Tour", "Concert", "Downtown Trip", "Bar crawl", "Excursion"]

#Random options
place = random.choice(destinations) 
food = random.choice(restaurants)
vehicle = random.choice(mode_transpo)
fun = random.choice(entertainmaent)

#Random Destination
def new_place(place_intro, place_dest): #
    result_place = place_intro + place_dest
    return result_place

result_place = new_place("Destination is: ",place)
print(result_place)

#Random Restaurant
def new_rest(rest_intro, rest_dine):
    result_rest = rest_intro + rest_dine
    return result_rest

result_rest = new_rest("Restaurant style is: ",food)
print(result_rest)

#Random Transportation
def new_trans(trans_intro, trans_sel):
    result_trans = trans_intro + trans_sel
    return result_trans

result_trans = new_trans("Transportation is: ", vehicle)
print(result_trans)

#Random Entertainment
def new_ent(ent_intro, ent_sel):
    result_ent = ent_intro + ent_sel
    return result_ent

result_ent = new_ent("Entertainment is: ", fun)
print (result_ent)

#Inquire Satisfaction
def print_inquire():
    result_inquire = ""
    return result_inquire

result_inquire = input("Are you satified with your trip? Y/N: ")
print(result_inquire) 

while  True:
    if result_inquire == "Y":
        print("Here is your trip")
        print(result_place)
        print(result_rest)
        print(result_trans)
        print(result_ent)
        print("Enjoy!")
        break

    elif result_inquire == "N":
         print(input("What do you want to change?: "))

    

   


# answer = "Destination"

# response + ''

# while ans
        

    





    
