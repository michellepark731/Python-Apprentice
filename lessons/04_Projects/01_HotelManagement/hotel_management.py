
"""

functions for checking guest in and out, using two dicts for guests and rooms, tuples and dicts using booleans
use tuple in a dict for each guests info

function for checking in:
    input (welcome to mocha hotels, would you like to check in or out?(checkin/checkout))
        input using dict (we have rooms 101, 102, 103, 104, 105)
        check in: make new key in dict, use the boolean varialbes for room availability
calling function for checking room availability based on room number

function for checking out, call based on input:
        checkout: probably check that the guest actually had a room, ask name, search name in guest dictionary?
use function to call for guests for this
            confirm identity
            say "thank you for staying at mocha hotels"
            remove guest from dict, update the room number to be True
            if guest is not found in dict 
            say "sorry, you're not a guest here. would you like to check in? (y/n)
            go back to check in function if y, break if n

call another function to update dictionaries when rooms are reserved using various inputs
    maybe entering something into terminal == room service, food?
        true = available
        false = occupied
        while True:
        assign room to guest
        while False:
        print("sorry, room is currently occupied by another guest. would you like to reserve another room?"
    if reswrving an open room, repeat process until guest finds a free room
    if all boolean variables are false, say "sorry, all rooms are occupied. come back later!"

function for number of nights
    input("how many nights?" (10 per night))
    based on number of nights, use function for multiplying and calculating cost
    print("this room costs $x! are you sure? (y/n)" 
        y = update guest dict

function for room service:
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
guests = {
}
def check_room_availability(room):

def room_service(richguest)

cost = n x 10
    """
def check_in(guest):
x = 10
print("Welcome to Mocha Hotel. There are " + len(room_numbers) + " rooms in the hotel.")
e = input("Do you want to make a reservation?(y/n)")
if e == "y":
        c == input("Which room would you like to stay in? We have rooms" + ['101', '102', '103', '104', '105']
        check_room_availability(c)
        if the room is available:
            n = input("How many nights will you be staying?")
            input("Your reservation will cost" + cost + " in total. Do you confirm your agreement of this price?" (y/n)
            if input == "y":
                r = "Great! Would you like room service throughout your stay? (y/n)")
                if r = "y":
                room_service(richguest)

"""
        