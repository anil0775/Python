"""
This program generates passages that are generated in mad-lib format
Author: Anil
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad libs has started"
name = raw_input("Enter your name: ")

print "Enter three adjectives below"
print "****************************"
adjective1 = raw_input("Enter first adjective: ")
adjective2 = raw_input("Enter second adjective: ")
adjective3 = raw_input("Enter third adjective: ")

print "Enter a verb"
print "************"
verb = raw_input("Enter a verb: ")

print "Enter two nouns below"
print "*********************"
noun1 = raw_input("Enter first noun: ")
noun2 = raw_input("Enter second noun: ")

print "Enter one input for each of the following"
print "*****************************************"
animal = raw_input("Enter an animal of your choice: ")
food = raw_input("Enter a food of your choice: ")
fruit = raw_input("Enter a fruit of your choice: ")
superhero = raw_input("Enter a superhero of your choice: ")
country = raw_input("Enter a country of your choice: ")
dessert = raw_input("Enter a dessert of your choice: ")
year = raw_input("Enter an year of your choice: ")

print STORY % (name, adjective1, adjective2, animal, food, verb, noun1, fruit, adjective3, name, superhero, name, country, name, dessert, name, year, noun2)























