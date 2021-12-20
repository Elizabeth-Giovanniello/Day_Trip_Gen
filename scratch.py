import random

def test():
    result_one =  transport_options = ["bus", "commercial airplane", "boat", "unicycle", "cruise ship", "taxi", "rental car", "seaplane", "private jet", "helicopter", "walking", "uber", "swimming", "gondola", "an RV", "train"]
    result_two = hawaii_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    result_three = nyc_transport = [transport_options[0], transport_options[1], transport_options[2], transport_options[3], transport_options[5], transport_options[6], transport_options[8], transport_options[10], transport_options[11], transport_options[15]]
    result_four = yellowstone_transport = [transport_options[0], transport_options[1], transport_options[3], transport_options[6], transport_options[7], transport_options[8], transport_options[9], transport_options[10], transport_options[11], transport_options[14]]
    result_five = bahamas_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    result_six = siberia_transport = [transport_options[1], transport_options[8], transport_options[9]]
    result_seven = tokyo_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    result_eight = venice_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12], transport_options[13]]
    return result_one, result_two, result_three, result_four, result_five, result_six, result_seven, result_eight



#we will choose the destination first so that the transport/restaurant/entertainment options can be destination-specific
def generate_destination():
    selection = random.randint(0, (len(destinations) - 1)) #generating random number to select from list
    #print(selection)
    destination = destinations[selection]
    #the following prompts user to confirm and accounts for all possible responses
    user_confirm = input(f"We have selected a destination of {destination} for you! Does this sound good? Enter y/n: ").lower()
    while user_confirm != "y":
        if user_confirm != "n":
            user_confirm = input("Sorry, this is not a valid entry. Please enter y or n to indicate yes or no: ").lower()
        while user_confirm == "n":
            if destinations == None or len(destinations) == 1:
                user_confirm = input("Sorry, you have rejected all available options. Would you like to start over? Enter y/n: ").lower()
                if user_confirm == "y":
                    generate_destination()
                while user_confirm != "y":
                    if user_confirm == "n":
                        destination = input("Sorry you were unsatisfied with our destinations. Enter your desired destination here: ")
                        print(f"Cool idea! Your destination is now set as {destination}. Now let's move on.")
                        return destination
                    else:
                        user_confirm = input("Sorry, this is not a valid entry. Please enter y or n to indicate yes or no: ").lower()
            else:
                destinations.pop(selection)
                selection = random.randint(0, (len(destinations) - 1))
                destination = destinations[selection]
                user_confirm = input(f"Oh, sorry you don't like this location. No worries, we can try something else! How about {destination}? Enter y/n: ").lower()
    if user_confirm == "y":
        print("Awesome! Now let's figure out how you're going to get there!") #might change this wording later
    return destination


    

destination = "Hawaii"

def generate_transport():
    transport_options = ["bus", "commercial airplane", "boat", "unicycle", "cruise ship", "taxi", "rental car", "seaplane", "private jet", "helicopter", "walking", "uber", "swimming", "gondola", "an RV", "train"]
    hawaii_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    nyc_transport = [transport_options[0], transport_options[1], transport_options[2], transport_options[3], transport_options[5], transport_options[6], transport_options[8], transport_options[10], transport_options[11], transport_options[15]]
    yellowstone_transport = [transport_options[0], transport_options[1], transport_options[3], transport_options[6], transport_options[7], transport_options[8], transport_options[9], transport_options[10], transport_options[11], transport_options[14]]
    bahamas_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    siberia_transport = [transport_options[1], transport_options[8], transport_options[9]]
    tokyo_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    venice_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12], transport_options[13]]
    if destination == "Hawaii":
        transport = random.choice(hawaii_transport)
        transport = confirm_choice(hawaii_transport, "transportation option", transport)
    elif destination == "New York City":
        transport = random.choice(nyc_transport)
        transport = confirm_choice(nyc_transport, "transportation option", transport)
    elif destination == "Yellowstone National Park":
        transport = random.choice(yellowstone_transport)
        transport = confirm_choice(yellowstone_transport, "transportation option", transport)
    elif destination == "the Bahamas":
        transport = random.choice(bahamas_transport)
        transport = confirm_choice(bahamas_transport, "transportation option", transport)
    elif destination == "Siberia":
        transport = random.choice(siberia_transport)
        transport = confirm_choice(siberia_transport, "transportation option", transport)
    elif destination == "Tokyo":
        transport = random.choice(tokyo_transport)
        transport = confirm_choice(tokyo_transport, "transportation option", transport)
    elif destination == "Venice":
        transport = random.choice(venice_transport)
        transport = confirm_choice(venice_transport, "transportation option", transport)
    else:
        transport = random.choice(transport_options)
        transport = confirm_choice(transport_options, "transportation option", transport)
    return transport

transport = generate_transport()


#FOR WHEN YOU ARE LESS TIRED: try switching the remove to pop and pop the value into a new variable, then append to add it to a new list. then under the "want to start over" thing, assign list = new_list to reset the list, THEN return the confirm choices function *completed 