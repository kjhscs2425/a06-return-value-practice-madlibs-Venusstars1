adjective0 = input("Give me an adjective: ")
noun0 = input("Give me a noun: ")
plural_noun= input("Give me a plural noun: ")
Person = input("Give me a person in room (female): ")
adjective1=input("Give me an adjective: ")
clothes= input("Give me an article of clothing: ")
noun1 = input("Give me a noun: ")
City = input("Give me a city: ")
plural_noun1 = input("Give me a plural noun: ")
adjective2= input("Give me an adjective: ")

story = f"There are many {adjective0} ways to choose a/n {noun0} to read. First, you could ask for \
recommendations from your friends and {plural_noun}. Just don't ask aunt {Person} she only reads \
{adjective1} books with {clothes} ripping goddesses on the cover. If you friends and family are no help, \
try checking out the {noun1} review in the {City} times. If the {plural_noun1} featured there are too \
{adjective2} for your taste, try something a little more bland and boring."

print(story)