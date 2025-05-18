
"""

functions for checking guest in and out, using two dicts for guests and rooms, tuples and dicts using booleans
use tuple in a dict for each guests info

function for checking in: 70% done, need to find a use for lists
    input (welcome to mocha hotels, would you like to check in or out?(checkin/checkout))
        input using dict (we have rooms 101, 102, 103, 104, 105)
        check in: make new key in dict, use the boolean varialbes for room availability
calling function for checking room availability based on room number
search up room number, find value, do boolean to trigger certain response for true and false

function for checking out, call based on input: done
        checkout: probably check that the guest actually had a room, ask name, search name in guest dictionary?
use function to call for guests for this
            confirm identity
            say "thank you for staying at mocha hotels"
            remove guest from dict, update the room number to be True
            if guest is not found in dict 
            say "sorry, you're not a guest here. would you like to check in? (y/n)
            go back to check in function if y, break if n

call another function to update dictionaries when rooms are reserved using various inputs done
    maybe entering something into terminal == room service, food?
        true = available
        false = occupied
        while True:
        assign room to guest
        while False:
        print("sorry, room is currently occupied by another guest. would you like to reserve another room?"
    if reswrving an open room, repeat process until guest finds a free room
    if all boolean variables are false, say "sorry, all rooms are occupied. come back later!"

function for number of nights done
    input("how many nights?" (10 per night))
    based on number of nights, use function for multiplying and calculating cost
    print("this room costs $x! are you sure? (y/n)" 
        y = update guest dict

function for room service: done
        "would you like some amazing room service for an extra $5 dollars? (y/n)"
        y = redefine variable of cost when they order room service, update guest info
    ask for cash or credit (cash/credit)
    payment is confirmed, print("thanks for staying at mocha hotels")
"""

room_numbers = {
    "101": True,
    "102": True,
    "103": True,
    "104": True,
    "105": True
}
guestcost = {
}
guestroom = {

}
              

def check_in():
    
    print("There are " + len(room_numbers) + " rooms in the hotel.")
    e = input("Do you want to make a reservation?(y/n)")
    if e == "y":
            check_room_availability()
            
    n = input("How many nights will you be staying?")
    cost = n * 10
    input("Your reservation will cost" + cost + " in total. Do you confirm your agreement of this price?(y/n)")
    if input == "y":
        guestcost[name] = guestcost[name] + cost
        r = input("Great! Would you like room service throughout your stay? (y/n)")
        if r == "y":
              room_service(name)
              if r == "n":
                    print("Thank you for staying at Mocha Hotels!")


         
def check_room_availability():
    c = input("Which room would you like to stay in? We have rooms" + ['101', '102', '103', '104', '105'])
    if room_numbers[c]==True:
        print("The room is available!")
        guestroom[name] = c
        room_numbers[c] = False
        if room_numbers[c]==False:
            print("Sorry, this room is currently occupied.")
            check_room_availability()

def room_service(name):
            guestcost[name] = guestcost[name] + 15

def check_out():
     del guestroom[name]
     room_numbers[c] = True
     print("Thank you for staying at Mocha Hotels. Enjoy the rest of your day!")
     
while True:
    name = input("Hello! Please enter your name.")
    trigger = input("Do you want to check in or out? (Check in/Check out)")
    if trigger == "Check in":
        check_in()
        if trigger == "Check out":
             check_out()
             break