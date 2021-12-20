import random

def generate_entertainment():
    if destination == "Hawaii":
        entertainment = random.choice(hawaii_entertainment)
        entertainment = confirm_choice(hawaii_entertainment, "entertainment option", entertainment)
    elif destination == "New York City":
        entertainment = random.choice(nyc_entertainment)
        entertainment = confirm_choice(nyc_entertainment, "entertainment option", entertainment)
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


def generate_entertainment():
    if destination == "Hawaii":
        ent_list = hawaii_entertainment
    elif destination == "New York City":
        ent_list = nyc_entertainment
    elif destination == "Yellowstone National Park":
        ent_list = yellowstone_entertainment
    elif destination == "the Bahamas":
        ent_list = bahamas_entertainment
    elif destination == "Siberia":
        ent_list = siberia_entertainment
    elif destination == "Tokyo":
        ent_list = tokyo_entertainment
    elif destination == "Venice":
        ent_list = venice_entertainment
    else:
        ent_list = general_entertainment
    entertainment = random.choice(ent_list)
    entertainment = confirm_choice(ent_list, "entertainment option", entertainment)
    return entertainment


