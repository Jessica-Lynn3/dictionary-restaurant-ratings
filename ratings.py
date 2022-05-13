"""Restaurant rating lister."""

def get_file_ratings(filename):
    """ Reads through restaurant ratings and prints them in order"""

# open file
    log_file = open(filename)

    restaurant_dictionary = {}

# read through the file-- by looping through
    for line in log_file:
        line = line.rstrip()
        line = line.split(':')
        #print(line)

        #identify what's a score and what's a rating
        # add those variables to a dictionary
        restaurant_dictionary[line[0]] = line[1]
        #print(restaurant_dictionary)  

    
    return restaurant_dictionary

def print_dictionary(restaurant_dict_sorted):
    restaurant_dict_items = restaurant_dict_sorted.items()

#  print out the dictionary in alphabetically
    restaurant_dict_sorted = sorted(restaurant_dict_items)
    for restaurant, rating in restaurant_dict_sorted:
        print(f"{restaurant} is rated at {rating}.")

#get_ratings('scores.txt')
def user_rates_restaurant(dictionary):

    #while True:
    restaurant_name = input('Name of restaurant: ')
    restaurant_score = int(input('This restaurants score: '))
    dictionary[restaurant_name] = restaurant_score
    #print(restaurant_name)
    #print(restaurant_score)
    #print(dictionary)

#promt user for restaurant name
#prompt for score
#add to dict
#print all 

file_dictionary = get_file_ratings('scores.txt')
print_dictionary(file_dictionary)
user_rates_restaurant(file_dictionary)
print_dictionary(file_dictionary)
