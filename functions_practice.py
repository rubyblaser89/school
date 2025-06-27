#!/usr/bin/python3

# ask for user input of names
animal_names = input("Please enter animal names: ")

#split user input into words
animals = animal_names.split(',')

#sort names
sorted_animals = sorted(animals)

print(sorted_animals)

# verify returned animal names are in a list
print(isinstance(sorted_animals, list))

# print only first three names in list
for i in range(0,3):
    print(sorted_animals[i])
 # index animal names
for index, animal in enumerate(sorted_animals):
    print(animal)





