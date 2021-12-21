#(5 points): As a developer, I want to make at least three commits with descriptive messages.
#(5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.
#(5 points): As a user, I want a destination to be randomly selected for my day trip.
#(5 points): As a user, I want a restaurant to be randomly selected for my day trip.
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
#(10 points): As a user, I want to display my completed trip in the console.
#(5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!




import random

def simulation():
    intro_message = "Welcome to the Day Trip Generator! If you aren't sure what you want to do for your vacation, you have come to the right place!"
    print(intro_message)

    destinations = ["Hawaii", "New York City", "Yellowstone National Park", "the Bahamas", "Siberia", "Tokyo", "Venice"]

    hawaii_restaurants = ["Mama's Fish House", "Lahaina Grill", "MW Restaurant", "Town", "Art Cafe Hemingway", "Sweet Home Cafe", "Da Poke Shack", "Star Noodle", "Heavenly", "Annie's Island Fresh Burgers", "Keoke's Paradise", "Palate Wine Bar and Restaurant", "Fatboy's", "Hilo Bay Cafe", "Marugame Udon"]
    nyc_restaurants = ["Katz's Delicatessen", "Peter Luger", "Lombardi's", "Keens Steakhouse", "Tavern on the Green", "the Rainbow Room", "Totonno's", "the Russian Tea Room", "Delmonico's", "Rao's", "Sbarro", "a hotdog cart"]
    yellowstone_restaurants = ["Old Faithful Snow Lodge Geyser Grill", "Old Faithful Inn Dining Room", "Old Faithful General Store Grill", "a campfire BBQ", "a sack lunch"]
    bahamas_restaurants = ["Tropic Breeze Beach Bar & Grill", "Shannas Cove Restaurant", "the Dunmore", "Firefly Bar & Grill", "Cafe Matisse", "Santanna's Bar & Grill", "Curley's"]
    siberia_restaurants = ["Beerman & Pelmeni", "Tiflis", "La Maison", "Expeditsia", "Odnazhdi v Amerikye", "Puppen Haus", "Reka 827", "Vechny Zov", "Slavyansky Bazar", "Chaynaya Sinyukha"]
    tokyo_restaurants = ["Bar Benfiddich", "Kotaro", "Tamawarai", "Isetan Shinjuku", "Yakitori Imai", "Tonki", "L'Effervescence", "Butagumi", "Quintessence", "Kikunoi Akasaka", "Sushi Saito", "Ishikawa", "Kyourakutei"]
    venice_restaurants = ["Al Paradiso", "San Polo", "Alle Testiere", "Castello", "Caffe Florian", "San Marco", "Trattoria al Gatto Nero", "Al Profeta", "Antica Sacrestia", "Frary's", "Taverna La Fenice", "Osteria La Zucca", "Venissa"]
    general_restaurants = ["McDonald's", "Subway", "Burger King", "Pizza Hut"]

    transport_options = ["bus", "commercial airplane", "boat", "unicycle", "cruise ship", "taxi", "rental car", "seaplane", "private jet", "helicopter", "walking", "uber", "swimming", "gondola", "an RV", "train"]
    hawaii_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    nyc_transport = [transport_options[0], transport_options[1], transport_options[2], transport_options[3], transport_options[5], transport_options[6], transport_options[8], transport_options[10], transport_options[11], transport_options[15]]
    yellowstone_transport = [transport_options[0], transport_options[1], transport_options[3], transport_options[6], transport_options[7], transport_options[8], transport_options[9], transport_options[10], transport_options[11], transport_options[14]]
    bahamas_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    siberia_transport = [transport_options[1], transport_options[8], transport_options[9]]
    tokyo_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12]]
    venice_transport = [transport_options[1], transport_options[2], transport_options[4], transport_options[7], transport_options[8], transport_options[9], transport_options[12], transport_options[13]]
    #maybe go back and make a distinction for continental us

    hawaii_entertainment = ["swimming with the dolphins", "snorkeling", "hanging out at Kehena black-sand beach", "hiking at Hawaii Volcanoes National Park", "hiking to Akaka Falls", "visiting the Ho'omaluhia Botanical Garden", "surfing", "scuba diving", "attending a waterfall and rainforest hike", "whale watching"]
    nyc_entertainment = ["visiting Times Square", "seeing a show on Broadway", "visiting the Statue of Liberty", "touring Ellis Island", "partaking in a Circle Line Cruise", "attending a free walking tour of the city", "riding to the top of the Empire State Building", "exploring Chinatown and Little Italy", "strolling around Central Park", "visiting the Central Park Zoo", "seeing the Big Apple Circus"]
    yellowstone_entertainment = ["watching geysers erupt", "seeing wild animals in their natrual habitat", "hiking in nature", "viewing canyons and waterfalls", "going white water rafting", "camping", "watching a rodeo", "going fishing", "looking for fossils"]
    bahamas_entertainment = ["scuba diving", "snorkeling", "taking a boat tour", "swimming with the pigs at Pig Beach", "perusing Versailles Gardens", "going bone fishing", "visiting the Forts of Nassau", "shopping at Port Lucaya Marketplace", "gambling at a casino", "visiting museums"]
    siberia_entertainment = ["visiting Lake Baikal", "hiking in the Altai Mountains", "freezing to death", "huddling over a fire for warmth", "being interrogated by the KGB", "shopping for fur"]
    tokyo_entertainment = ["visiting the Yayoi Kusama Museum", "exploring the Shinjuku Gyoen National Garden", "visiting the Senso-ji temple", "shopping at Tsukiji Market", "admiring the cherry blossoms at Nakameguro", "spectating a Sumo tournament at Ryogoku Kokugikan", "seeing origami at Origami Kaikan"]
    venice_entertainment = ["visiting St. Mark's Basilica", "touring the Grand Canal", "roaming the canals in a gondola while being serenaded by a world-class Italian opera singer", "seeing an Italian opera at Teatro La Fenice", "exploring Piazza San Marco", "touring Palazzo Ducale", "attending a glass blowing demonstration and glass factory tour", "visiting Correr Civic Museum"]
    general_entertainment = ["seeing a movie", "seeing a show", "attending a walking tour to explore the area", "going to all the tourist traps", "conversing with the locals", "shopping for souvenirs", "going to museums", "observing the wildlife"]

    all_restaurants = [hawaii_restaurants, nyc_restaurants, yellowstone_restaurants, bahamas_restaurants, siberia_restaurants, tokyo_restaurants, venice_restaurants, general_restaurants]
    all_transport = [hawaii_transport, nyc_transport, yellowstone_transport, bahamas_transport, siberia_transport, tokyo_transport, venice_transport, transport_options]
    all_entertainment = [hawaii_entertainment, nyc_entertainment, yellowstone_entertainment, bahamas_entertainment, siberia_entertainment, tokyo_entertainment, venice_entertainment, general_entertainment]

    destination = generate_destination(destinations)
    transport = generate_transport(destination, all_transport)
    entertainment = generate_entertainment(destination, all_entertainment)
    restaurant = generate_restaurant(destination, all_restaurants)

    finalize_trip(destination, transport, entertainment, restaurant, destinations, all_transport, all_entertainment, all_restaurants)
    



def confirm_choice(list, category_sing, result):
    new_list = []
    user_confirm = input(f"We have selected {result} for your {category_sing}! Does this sound good? Enter y/n: ").lower()
    while user_confirm != "y":
            if user_confirm != "n":
             user_confirm = input("Sorry, this is not a valid entry. Please enter y or n to indicate yes or no: ").lower()
            while user_confirm == "n":
                if list == None or len(list) == 1:
                    user_confirm = input("Sorry, you have rejected all available options. Would you like to start over? Enter y/n: ").lower()
                    if user_confirm == "y":
                        list.remove(result) 
                        new_list.append(result)
                        list = new_list
                        return confirm_choice(list, category_sing, result)
                    while user_confirm != "y":
                        if user_confirm == "n":
                            result = input(f"Sorry you were unsatisfied with our {category_sing}s. Enter your desired {category_sing} here: ")
                            print(f"Cool idea! Your {category_sing} is now set as {result}. Now let's move on.")
                            return result
                        else:
                            user_confirm = input("Sorry, this is not a valid entry. Please enter y or n to indicate yes or no: ").lower()
                else:
                    list.remove(result)
                    new_list.append(result)
                    result = random.choice(list)
                    user_confirm = input(f"Oh, sorry you don't like this {category_sing}. No worries, we can try something else! How about {result}? Enter y/n: ").lower()
    if user_confirm == "y":
        print("Awesome! Glad that is decided. Let's move on!") #might change this wording later
    return result



#we will choose the destination first so that the transport/restaurant/entertainment options can be destination-specific
def generate_destination(destinations):
    destination = random.choice(destinations)
    destination = confirm_choice(destinations[:], "destination", destination)
    return destination



#instead of generating transportation options from the same list regardless of location, we will use a function that picks
#from a list specific to the selected location, so we aren't taking a boat to siberia or driving to hawaii



def generate_transport(destination, all_transport):
    if destination == "Hawaii":
        transp_list = all_transport[0][:]
    elif destination == "New York City":
        transp_list = all_transport[1][:]
    elif destination == "Yellowstone National Park":
        transp_list = all_transport[2][:]
    elif destination == "the Bahamas":
        transp_list = all_transport[3][:]
    elif destination == "Siberia":
        transp_list = all_transport[4][:]
    elif destination == "Tokyo":
        transp_list = all_transport[5][:]
    elif destination == "Venice":
        transp_list = all_transport[6][:]
    else:
        transp_list = all_transport[7][:]
    transport = random.choice(transp_list)
    transport = confirm_choice(transp_list, "transportation option", transport)
    return transport




def generate_entertainment(destination, all_entertainment):
    if destination == "Hawaii":
        ent_list = all_entertainment[0][:]
    elif destination == "New York City":
        ent_list = all_entertainment[1][:]
    elif destination == "Yellowstone National Park":
        ent_list = all_entertainment[2][:]
    elif destination == "the Bahamas":
        ent_list = all_entertainment[3][:]
    elif destination == "Siberia":
        ent_list = all_entertainment[4][:]
    elif destination == "Tokyo":
        ent_list = all_entertainment[5][:]
    elif destination == "Venice":
        ent_list = all_entertainment[6][:]
    else:
        ent_list = all_entertainment[7][:]
    entertainment = random.choice(ent_list)
    entertainment = confirm_choice(ent_list, "entertainment option", entertainment)
    return entertainment


def generate_restaurant(destination, all_restaurants):
    if destination == "Hawaii":
        rest_list = all_restaurants[0][:]
    elif destination == "New York City":
        rest_list = all_restaurants[1][:]
    elif destination == "Yellowstone National Park":
        rest_list = all_restaurants[2][:]
    elif destination == "the Bahamas":
        rest_list = all_restaurants[3][:]
    elif destination == "Siberia":
        rest_list = all_restaurants[4][:]
    elif destination == "Tokyo":
        rest_list = all_restaurants[5][:]
    elif destination == "Venice":
        rest_list = all_restaurants[6][:]
    else:
        rest_list = all_restaurants[7][:]
    restaurant = random.choice(rest_list)
    restaurant = confirm_choice(rest_list, "restaurant", restaurant)
    return restaurant





def finalize_trip(destination, transport, entertainment, restaurant, destinations, all_transport, all_entertainment, all_restaurants):
    print("Congrats! We have completed generating your day trip. Now let's just confirm that this is the trip you wanted. ")
    print("The trip we have generated for you is: ")
    print(f"Destination: {destination}")
    print(f"Transportation: {transport}")
    print(f"Restaurant: {restaurant}")
    print(f"Entertainment: {entertainment}")
    user_answer = input("Would you like to finalize this trip? Enter y/n: ").lower()
    while user_answer != "y":
        if user_answer == "n":
            change = input("You have opted not to confirm this trip. Which aspect of the trip would you like to change? Enter d to change the destination, t to change the transportation, r to change the restaurant, e to change the entertainment, or c to confirm the current selection. ").lower()
            if change == "d":
                destination = generate_destination(destinations)
                transport = generate_transport(destination, all_transport)
                entertainment = generate_entertainment(destination, all_entertainment)
                restaurant = generate_restaurant(destination, all_restaurants)
                return finalize_trip(destination, transport, entertainment, restaurant, destinations, all_transport, all_entertainment, all_restaurants)
            elif change == "t":
                transport = generate_transport(destination, all_transport)
                return finalize_trip(destination, transport, entertainment, restaurant, destinations, all_transport, all_entertainment, all_restaurants)
            elif change == "e":
                entertainment = generate_entertainment(destination, all_entertainment)
                return finalize_trip(destination, transport, entertainment, restaurant, destinations, all_transport, all_entertainment, all_restaurants)
            elif change == "r":
                restaurant = generate_restaurant(destination, all_restaurants)
                return finalize_trip(destination, transport, entertainment, restaurant, destinations, all_transport, all_entertainment, all_restaurants)
            elif change == "c":
                print(f"Prepare for your dream vacation to come alive! You will be arriving in {destination} by {transport}, where you will spend the day {entertainment}. You will end the evening dining in style at {restaurant}, a famous local restaurant. ")
            else:
                print("Sorry, this is not a valid entry. Let's try this again.")
                return finalize_trip(destination, transport, entertainment, restaurant, destinations, all_transport, all_entertainment, all_restaurants)
        elif user_answer != "n": 
            user_answer = input("Sorry, this is not a valid entry. Please enter y or n to indicate yes or no: ").lower()
    if user_answer == "y":
        print(f"Prepare for your dream vacation to come alive! You will be arriving in {destination} by {transport}, where you will spend the day {entertainment}. You will end the evening dining in style at {restaurant}, a famous local restaurant. ")


    

simulation()


#add comments for clarity
#figure out why finalize trip function isn't having it work when you go through the list again
#finish creating entertainment list
#double check everything
#double check grammar in quoted parts