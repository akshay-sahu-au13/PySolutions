# Program to print Vowel in a given string.

Str = input("Please enter a string: \n")

Vowel = "AEIOUaeiou"

print("Here is the list of Vowel in the provided string:\n")

N = 0

for i in Str:

    if i in Vowel:

        print(i)

        N+=1

if N == 0:
    print("Vowels not found in given string")   

