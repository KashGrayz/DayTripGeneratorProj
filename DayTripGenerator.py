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
def new_place(place_intro, place_dest): 
    result_place = place_intro + place_dest
    return result_place

result_place = new_place("1. Destination is: ",place)
print(result_place)

#Random Restaurant
def new_rest(rest_intro, rest_dine):
    result_rest = rest_intro + rest_dine
    return result_rest

result_rest = new_rest("2. Restaurant style is: ",food)
print(result_rest)

#Random Transportation
def new_trans(trans_intro, trans_sel):
    result_trans = trans_intro + trans_sel
    return result_trans

result_trans = new_trans("3. Transportation is: ", vehicle)
print(result_trans)

#Random Entertainment
def new_ent(ent_intro, ent_sel):
    result_ent = ent_intro + ent_sel
    return result_ent

result_ent = new_ent("4. Entertainment is: ", fun)
print (result_ent)

#Inquire Satisfaction
# def print_inquire():
#     result_inquire = ""
#     return result_inquire

# result_inquire = input()
# print(result_inquire)

def option_1(opt1_intro, opt1_place):
    option_1_answer = opt1_intro + opt1_place
    return option_1_answer
option_1_answer = option_1("1. Destination is: ",random.choice(destinations))

option = True

while option is True:
    result_inquire = input("Are you satified with your trip? Y/N: ")
    print(result_inquire)
    if result_inquire == "Y":
            print("Here is your trip")
            print(result_place)
            print(result_rest)
            print(result_trans)
            print(result_ent)
            break

    elif result_inquire == "N":
        continue
        

satisfaction = input("What would you like to change 1-4?:  ")

while satisfaction == "1":
    print("Here is your trip")
    print(option_1_answer)
    print(result_rest)
    print(result_trans)
    print(result_ent)
    result_inquire = input("Are you satified with your trip? Y/N: ")
    

    if result_inquire == "N":
        satisfaction = input("What would you like to change 1-4?:  ")
        print(satisfaction)
        continue
print ("Enjoy!")
       
def option_2(opt2_intro, opt2_place):
    option_2_answer = opt2_intro + opt2_place
    return option_2_answer
option_2_answer = option_2(". Restaurant style is: ",random.choice(food))






  

