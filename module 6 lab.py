import math
# package sizes
DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

def main():
    # total number of hot dogs needed
    total_hot_dogs = get_total_hot_dogs()

    #  minimum number of packages and leftovers
    dogs_leftover = (DOGS_PER_PACKAGE - total_hot_dogs % DOGS_PER_PACKAGE) % DOGS_PER_PACKAGE
    min_dogs = math.ceil(total_hot_dogs / DOGS_PER_PACKAGE)

    buns_leftover = (BUNS_PER_PACKAGE - total_hot_dogs % BUNS_PER_PACKAGE) % BUNS_PER_PACKAGE
    min_buns = math.ceil(total_hot_dogs / BUNS_PER_PACKAGE)

    # Display the results
    show_results(dogs_leftover, min_dogs, buns_leftover, min_buns)

def get_total_hot_dogs():
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs_per_person = int(input("Enter the number of hot dogs for each person: "))

    # total number of hot dogs needed
    total_hot_dogs = people * hot_dogs_per_person
    return total_hot_dogs

def show_results(dogs_leftover, min_dogs, buns_leftover, min_buns):
    #minimum packages of hot dogs needed
    print("Minimum packages of hot dogs needed:", min_dogs)

    # minimum packages of buns needed
    print("Minimum packages of hot dog buns needed:", min_buns)

    #  number of hot dogs left over
    print("Hot dogs left over:", dogs_leftover)

    #  number of hot dog buns left over
    print("Hot dog buns left over:", buns_leftover)

main()

